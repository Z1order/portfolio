# portfolio

Every project in one place, at <https://z1order.github.io/portfolio/>.

The site is generated from `content/*.md` — one markdown file per project, with
a few lines of frontmatter and some prose. Adding a project means adding a file;
there is no index to update and no HTML to edit.

## Building

Python 3, standard library only. Nothing to install.

```bash
python3 build.py
```

Output lands in `_site/`, which is generated and not committed. To preview:

```bash
python3 build.py --serve
```

Then open <http://localhost:8000>.

## Deploying

Push to `main`. The workflow in `.github/workflows/pages.yml` runs `build.py`
and publishes `_site/` to GitHub Pages. Nothing needs building locally first.

## Layout

| Path | What it is |
|---|---|
| `content/*.md` | One file per project. The only thing you normally edit. |
| `content/_TEMPLATE.md` | Starting point for a new project. Underscore-prefixed files are skipped by the build. |
| `assets/` | Screenshots, copied through to the site as-is. |
| `build.py` | The whole generator, ~200 lines. |
| `style.css` | Light and dark, no framework. |
| `CLAUDE.md` | Conventions — read this before adding a project. |
| `NOTES.md` | Private working notes. **Gitignored**, never published. |

## A note on what is public

This repository and the site it builds are both public. App Store Connect
identifiers, submission dates and rejection history stay in `NOTES.md`, which is
gitignored. See `CLAUDE.md` for where the line sits.
