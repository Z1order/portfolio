#!/usr/bin/env python3
"""Compare content/*.md against what App Store Connect actually says.

Two things go stale by hand and are checked here:

  status  — Apple approves something and the file still says "Ready to submit".
  title   — the listing name changes and the site keeps showing the old one.
            HW Schedule shipped as "Block Day: Rotating Schedule"; nothing in
            this repo would have noticed.

    python3 check_status.py

Exits non-zero if anything disagrees, so it can gate a commit if you want it to.

The live-app half uses the public iTunes lookup API — no key, no auth. That is
the half that always runs. Unreleased app records are invisible to that API, so
their names are only checked when ASC_SCRIPT (below) is configured.
"""

import json
import subprocess
import sys
import urllib.request
from pathlib import Path

from build import CONTENT, parse

# The developer account these apps ship under. Find it in any app's lookup
# response as `artistId`.
ARTIST_ID = "1070055621"
API = "https://itunes.apple.com/lookup?id={}&entity=software&limit=200&country=us"

# Records under this account that are not portfolio projects. Reported as known
# and ignored rather than as problems, so a clean run really does exit 0.
IGNORED_BUNDLES = {
    "com.aariz.2LetterSightWords": "another developer's app, unrelated",
    "com.aariz.icerunner":         "another developer's app, unrelated",
    "com.zidaan.Larder":           "Supper's old name; Apple cannot delete a record",
}

# Slugs whose bundle id is not just the slug with the hyphens taken out.
BUNDLE_OVERRIDES = {
    "hw-schedule":      "com.zidaan.hwschedule",
    "homework-planner": "com.zidaan.homeworkplanner",
    "wrist-checkers":   "com.zidaan.checkers",
}

# Path to an App Store Connect API client, relative to this file. That script
# carries the key id and issuer id, which is why it lives outside this public
# repository and is named in a gitignored file rather than committed here.
#
#   echo '{"ascScript": "../Morsel/AppStore/asc.rb"}' > .asc.json
#
# Without it the unreleased-name check is skipped and everything else still runs.
ASC_CONFIG = Path(__file__).parent / ".asc.json"


def store_apps():
    with urllib.request.urlopen(API.format(ARTIST_ID), timeout=20) as r:
        results = json.load(r)["results"]
    return [a for a in results if a.get("wrapperType") == "software"]


def all_app_records():
    """Every app record, including ones with no public listing yet.

    Returns {bundleId: name}, or None when no client is configured.
    """
    if not ASC_CONFIG.exists():
        return None
    script = (Path(__file__).parent / json.loads(ASC_CONFIG.read_text())["ascScript"]).resolve()
    if not script.exists():
        print(f"warning: {ASC_CONFIG.name} points at {script}, which is not there")
        return None
    out = subprocess.run(
        ["ruby", str(script), "/v1/apps?limit=200&fields[apps]=name,bundleId"],
        capture_output=True, text=True, timeout=60,
        env={"RUBYOPT": "-EUTF-8", "PATH": "/usr/bin:/bin:/usr/local/bin", "HOME": str(Path.home())},
    )
    if out.returncode != 0:
        print(f"warning: could not reach App Store Connect: {out.stderr.strip()[:200]}")
        return None
    body = out.stdout.split("\n", 1)[1]          # asc.rb prints "HTTP 200" first
    return {a["attributes"]["bundleId"]: a["attributes"]["name"]
            for a in json.loads(body)["data"]}


def bundle_for(slug, known):
    if slug in BUNDLE_OVERRIDES:
        return BUNDLE_OVERRIDES[slug]
    want = slug.replace("-", "")
    return next((b for b in known if b.split(".")[-1].lower() == want), None)


def matches(title, track_name):
    """A title and a listing name refer to the same app.

    Titles are the full listing name now, so this is usually equality. It stays
    loose because it also has to pair a file with its app when one of the two is
    mid-rename — which is the case worth reporting, not hiding.
    """
    a, b = title.lower(), track_name.lower()
    return a in b or b in a


def main():
    docs = [parse(p) for p in sorted(CONTENT.glob("*.md"))
            if not p.name.startswith("_")]
    try:
        live = store_apps()
    except Exception as e:                      # offline, rate-limited, whatever
        print(f"Could not reach the App Store API: {e}")
        return 2

    shown = [a for a in live if a.get("bundleId") not in IGNORED_BUNDLES]
    print(f"{len(shown)} app(s) live under artist {ARTIST_ID}:")
    for a in shown:
        print(f"  {a['trackName']!r}  v{a.get('version')}  "
              f"{a.get('releaseDate','')[:10]}  id={a['trackId']}")
    print()

    problems = []

    for doc in docs:
        hit = next((a for a in live if matches(doc["title"], a["trackName"])), None)
        if hit and doc["status"] != "Live":
            problems.append(
                f"{doc['slug']}.md says {doc['status']!r} but "
                f"{hit['trackName']!r} has been on the store since "
                f"{hit.get('releaseDate','')[:10]} "
                f"(id={hit['trackId']}) — set status to Live and add the link")
        elif not hit and doc["status"] == "Live" and doc["kind"] == "Apple app":
            problems.append(
                f"{doc['slug']}.md says 'Live' but no matching app is on the store")
        # The title has to be the listing name exactly, or the site and the
        # App Store link it carries disagree about what the app is called.
        if hit and doc["title"] != hit["trackName"]:
            problems.append(
                f"{doc['slug']}.md is titled {doc['title']!r} but the listing is "
                f"{hit['trackName']!r} — set title to the listing name")

    for a in live:
        if a.get("bundleId") in IGNORED_BUNDLES:
            continue
        if not any(matches(d["title"], a["trackName"]) for d in docs):
            problems.append(
                f"{a['trackName']!r} (id={a['trackId']}, "
                f"{a.get('bundleId')}) is on the store with no content file")

    # Unreleased records: names only, since there is no status to check yet.
    records = all_app_records()
    if records is None:
        print("Unreleased app names not checked — see ASC_CONFIG in this file.\n")
    else:
        live_bundles = {a.get("bundleId") for a in live}
        for doc in docs:
            bid = bundle_for(doc["slug"], records)
            if bid is None or bid in live_bundles or bid in IGNORED_BUNDLES:
                continue                        # unmatched, or already checked above
            if doc["title"] != records[bid]:
                problems.append(
                    f"{doc['slug']}.md is titled {doc['title']!r} but its app record "
                    f"is {records[bid]!r} — set title to the listing name")
        matched = {bundle_for(d["slug"], records) for d in docs}
        for bid, name in sorted(records.items()):
            if bid not in matched and bid not in IGNORED_BUNDLES:
                problems.append(
                    f"{name!r} ({bid}) has an app record but no content file")

    known = [(b, why) for b, why in IGNORED_BUNDLES.items()]
    if known:
        print("Known and ignored:")
        for b, why in known:
            print(f"  {b} — {why}")
        print()

    if not problems:
        print("Everything agrees.")
        return 0
    print(f"{len(problems)} disagreement(s):")
    for p in problems:
        print(f"  - {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
