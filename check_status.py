#!/usr/bin/env python3
"""Compare the `status:` in content/*.md against what is actually on the App Store.

The statuses in this repo are written by hand, so they go stale the moment Apple
approves something — which is exactly what happened to Homework Planner and
Wrist Checkers. This asks Apple instead of trusting the files.

    python3 check_status.py

Exits non-zero if anything disagrees, so it can gate a commit if you want it to.
Uses the public iTunes lookup API — no key, no auth, read-only.
"""

import json
import sys
import urllib.request
from pathlib import Path

from build import CONTENT, parse

# The developer account these apps ship under. Find it in any app's lookup
# response as `artistId`.
ARTIST_ID = "1070055621"
API = "https://itunes.apple.com/lookup?id={}&entity=software&limit=200&country=us"


def store_apps():
    with urllib.request.urlopen(API.format(ARTIST_ID), timeout=20) as r:
        results = json.load(r)["results"]
    return [a for a in results if a.get("wrapperType") == "software"]


def matches(title, track_name):
    """Listing names carry a descriptor the portfolio title does not
    ("Homework Planner" vs "Homework Planner for Students")."""
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

    print(f"{len(live)} app(s) live under artist {ARTIST_ID}:")
    for a in live:
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

    for a in live:
        if not any(matches(d["title"], a["trackName"]) for d in docs):
            problems.append(
                f"{a['trackName']!r} (id={a['trackId']}, "
                f"{a.get('bundleId')}) is on the store with no content file")

    if not problems:
        print("Everything agrees.")
        return 0
    print(f"{len(problems)} disagreement(s):")
    for p in problems:
        print(f"  - {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
