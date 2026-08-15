# Working in this repository

This is the portfolio site at <https://z1order.github.io/portfolio/>. It lists
every project in `~/Developer/Projects` with a page each.

**The whole site is generated from `content/*.md`.** One file per project. There
is no other place a project is registered — no index to update, no nav to edit,
no HTML to touch. Add a file, and it appears.

## Adding a project

1. Copy `content/_TEMPLATE.md` to `content/<slug>.md`. The filename becomes the
   URL: `content/warranty.md` → `/warranty/`. Use lowercase and hyphens.
2. Fill in the frontmatter (everything above the `---` line). See the field
   reference below.
3. Optionally drop a screenshot in `assets/<slug>.png` and set `image:` to that
   filename. Portrait phone screenshots look right; anything works.
4. Run `python3 build.py` and open `_site/index.html` to check it.
5. Commit and push. GitHub Actions rebuilds and deploys — you do **not** commit
   `_site/`, it is generated and gitignored.

## Editing a project

Edit its `content/*.md` file and push. Nothing else refers to it.

## Frontmatter fields

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Display name. |
| `kind` | yes | One of `Apple app`, `Game`, `Web`, `Experiment`, `Other`. Sets which section of the index it lands in. |
| `status` | yes | One of `Live`, `In App Store review`, `Ready to submit`, `In development`, `Archived`. Renders as a coloured badge. |
| `tagline` | yes | One line, plain language, no marketing voice. Shows on the card and under the title. |
| `order` | no | Sort position within its section. Defaults to 999, then alphabetical. |
| `platforms` | no | e.g. `iPhone, iPad, Mac`. |
| `stack` | no | e.g. `SwiftUI, SwiftData, CloudKit`. |
| `image` | no | Filename in `assets/`. |
| `links` | no | `Label \| URL` pairs separated by `;`. |

To add a new `kind` or `status`, edit the `KINDS` / `STATUSES` tables at the top
of `build.py`; a new status also needs a colour rule in `style.css`. `build.py`
fails loudly on an unknown value rather than silently dropping the project.

## Body markup

A deliberately small markdown subset — `## headings`, paragraphs, `- bullets`,
`**bold**`, `` `code` `` and `[links](url)`. That is all `build.py` implements.
Anything else will render literally, which is the intended failure: it is
visible rather than silent. Extend `markdown()` in `build.py` if you genuinely
need more.

## What goes on this site, and what does not

The site is **public and indexed**. Keep off it:

- App Store Connect Apple IDs, SKUs, the developer team ID
- Rejection history, review correspondence, submission dates
- Anything about an unreleased app you would not want a competitor reading

That material lives in `NOTES.md`, which is **gitignored** — it stays on this
machine and is never pushed. Read it for context when working on an app; do not
copy from it into `content/`.

For `status`, prefer the broad public-facing label over the specific truth.
"In App Store review" covers submitted, rejected-and-responding, and awaiting
review alike. That is deliberate.

## House style for the prose

Match the existing entries. They are written to be read by a person who does not
already know the app:

- Open with what it does and who it is for. No throat-clearing.
- The **Worth knowing** section is the point of each page — the one genuinely
  interesting constraint or decision. Write the thing that was hard, not the
  thing anyone would guess. If nothing was hard, leave the section out.
- No superlatives, no "seamless", no "powerful". The apps are small and the
  writing should be too.

## Related

The per-app marketing sites (`../warranty-site`, `../streak-site` and so on) are
separate repositories with their own privacy and support pages, which the App
Store requires. This portfolio links to them; it does not replace them.
