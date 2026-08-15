#!/usr/bin/env python3
"""Build the portfolio site from content/*.md into _site/.

One markdown file per project. Nothing else needs editing to add a project —
drop a file in content/, run this, and it appears on the index and gets its own
page. Standard library only, so there is nothing to install.

    python3 build.py            # build into _site/
    python3 build.py --serve    # build, then serve _site/ on :8000
"""

import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
OUT = ROOT / "_site"

SITE_TITLE = "Zidaan Furniturewala"
SITE_BLURB = ("Apps, games and experiments. Mostly Swift on Apple platforms, "
              "some C# in Godot. No servers, no accounts, no tracking.")

# Cards are grouped under these headings, in this order. A project's `kind`
# must match one of them; anything else lands in "Other".
KINDS = ["Apple app", "Game", "Web", "Experiment", "Other"]

# Status label -> CSS modifier. Add a new status here and in style.css.
STATUSES = {
    "Live": "live",
    "In App Store review": "review",
    "Ready to submit": "ready",
    "In development": "wip",
    "Archived": "archived",
}


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

def parse(path):
    """Split a content file into a dict of fields plus a markdown body.

    Frontmatter is `key: value` lines, ended by a line of `---`. Values are
    plain text; `links` is special-cased as `Label | URL` pairs separated by
    semicolons.
    """
    raw = path.read_text(encoding="utf-8")
    if "\n---\n" not in raw:
        raise SystemExit(f"{path.name}: no `---` line separating frontmatter from body")
    head, body = raw.split("\n---\n", 1)

    doc = {"slug": path.stem, "links": [], "order": "999"}
    for n, line in enumerate(head.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise SystemExit(f"{path.name} line {n}: expected `key: value`, got {line!r}")
        key, value = line.split(":", 1)
        doc[key.strip()] = value.strip()

    if "links" in doc and isinstance(doc["links"], str):
        pairs = []
        for chunk in doc["links"].split(";"):
            chunk = chunk.strip()
            if not chunk:
                continue
            if "|" not in chunk:
                raise SystemExit(f"{path.name}: link {chunk!r} is not `Label | URL`")
            label, url = chunk.split("|", 1)
            pairs.append((label.strip(), url.strip()))
        doc["links"] = pairs

    for required in ("title", "kind", "status", "tagline"):
        if required not in doc:
            raise SystemExit(f"{path.name}: missing required field `{required}`")
    if doc["status"] not in STATUSES:
        raise SystemExit(
            f"{path.name}: unknown status {doc['status']!r}. "
            f"Known: {', '.join(STATUSES)}")

    doc["body"] = body.strip()
    return doc


# --------------------------------------------------------------------------
# A deliberately small markdown subset: ## headings, paragraphs, - bullets,
# **bold**, `code` and [links](url). Enough for prose about a project.
# --------------------------------------------------------------------------

def inline(text):
    """Escape, then apply inline markup. Code spans are held out of the way
    first so their contents are never treated as bold or as a link."""
    spans = []

    def stash(m):
        spans.append(html.escape(m.group(1)))
        return f"\x00{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # Bold before italic: once **...** is consumed, any asterisk left is italic.
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{spans[int(m.group(1))]}</code>", text)


def markdown(src):
    out = []

    def bullet_list(block):
        """A bullet runs until the next `- `. Wrapped continuation lines belong
        to the bullet above them, not to a new one."""
        items = []
        for line in block.splitlines():
            line = line.strip()
            if line.startswith("- "):
                items.append(line[2:].strip())
            elif items:
                items[-1] += " " + line
            else:
                items.append(line)
        return "<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"

    for block in re.split(r"\n\s*\n", src.strip()):
        block = block.strip()
        if not block:
            continue
        if block.startswith("## "):
            out.append(f"<h2>{inline(block[3:].strip())}</h2>")
        elif block.startswith("- "):
            out.append(bullet_list(block))
        else:
            out.append(f"<p>{inline(' '.join(block.split()))}</p>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

def page(title, description, body, depth=0):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<div class="wrap">
{body}
<footer>
	<p>Built from <code>content/</code> by <code>build.py</code>. Source on
	<a href="https://github.com/Z1order/portfolio">GitHub</a>.</p>
</footer>
</div>
</body>
</html>
"""


def badge(status):
    return f'<span class="badge {STATUSES[status]}">{html.escape(status)}</span>'


def card(doc):
    # The index shows app icons, not screenshots — at 56px a screenshot is an
    # unreadable smudge, whereas an icon is designed to be recognised at that
    # size. Projects with no icon of their own get a monogram tile.
    if doc.get("icon"):
        mark = (f'<img class="icon" src="assets/icons/{html.escape(doc["icon"])}" '
                f'alt="" loading="lazy">')
    else:
        mark = f'<span class="icon monogram" aria-hidden="true">{html.escape(doc["title"][0])}</span>'
    meta = html.escape(doc.get("platforms", ""))
    return f"""<a class="card" href="{html.escape(doc['slug'])}/">
	{mark}
	<div class="card-text">
		<h3>{html.escape(doc['title'])} {badge(doc['status'])}</h3>
		<p>{html.escape(doc['tagline'])}</p>
		<p class="meta">{meta}</p>
	</div>
</a>"""


def index(docs):
    sections = []
    for kind in KINDS:
        group = [d for d in docs if d["kind"] == kind]
        if not group:
            continue
        cards = "\n".join(card(d) for d in group)
        plural = kind if kind.endswith("s") else kind + "s"
        sections.append(
            f'<h2 class="section">{html.escape(plural)}</h2>\n'
            f'<div class="grid">\n{cards}\n</div>')

    body = f"""<header class="site">
	<h1>{html.escape(SITE_TITLE)}</h1>
	<p class="lede">{html.escape(SITE_BLURB)}</p>
</header>
{"".join(sections)}"""
    return page(SITE_TITLE, SITE_BLURB, body)


def detail(doc):
    rows = []
    for label, key in (("Platforms", "platforms"), ("Built with", "stack")):
        if doc.get(key):
            rows.append(f"<dt>{label}</dt><dd>{html.escape(doc[key])}</dd>")
    rows.append(f"<dt>Status</dt><dd>{badge(doc['status'])}</dd>")
    if doc["links"]:
        joined = " · ".join(
            f'<a href="{html.escape(u)}">{html.escape(l)}</a>' for l, u in doc["links"])
        rows.append(f"<dt>Links</dt><dd>{joined}</dd>")

    shot = ""
    if doc.get("image"):
        shot = (f'<img class="hero-shot" src="../assets/{html.escape(doc["image"])}" '
                f'alt="A screen from {html.escape(doc["title"])}.">')

    body = f"""<header class="site">
	<nav class="sub"><a href="../">&larr; All projects</a></nav>
	<h1>{html.escape(doc['title'])}</h1>
	<p class="lede">{html.escape(doc['tagline'])}</p>
</header>
{shot}
<dl class="facts">{"".join(rows)}</dl>
{markdown(doc['body'])}"""
    return page(f"{doc['title']} — {SITE_TITLE}", doc["tagline"], body, depth=1)


# --------------------------------------------------------------------------

def build():
    files = sorted(p for p in CONTENT.glob("*.md") if not p.name.startswith("_"))
    if not files:
        raise SystemExit("content/ has no project files")
    docs = sorted((parse(p) for p in files),
                  key=lambda d: (KINDS.index(d["kind"]) if d["kind"] in KINDS
                                 else len(KINDS), int(d["order"]), d["title"]))

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    (OUT / "index.html").write_text(index(docs), encoding="utf-8")
    for doc in docs:
        page_dir = OUT / doc["slug"]
        page_dir.mkdir()
        (page_dir / "index.html").write_text(detail(doc), encoding="utf-8")

    shutil.copy(ROOT / "style.css", OUT / "style.css")
    (OUT / ".nojekyll").write_text("")
    if ASSETS.exists():
        shutil.copytree(ASSETS, OUT / "assets", dirs_exist_ok=True)

    print(f"Built {len(docs)} projects into {OUT.relative_to(ROOT)}/")
    for doc in docs:
        print(f"  {doc['slug']:<24} {doc['kind']:<12} {doc['status']}")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print("\nhttp://localhost:8000  (ctrl-c to stop)")
        http.server.HTTPServer(("", 8000), handler).serve_forever()
