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
3. Optionally add art:
   - **Icon** — `assets/icons/<slug>.png`, set `icon:`. This is what the index
     shows. Pull the 1024×1024 from the project's
     `Assets.xcassets/AppIcon.appiconset/AppIcon.png` and downscale it:
     `sips -Z 128 <src> --out assets/icons/<slug>.png`. Ship the flat square —
     the rounding is CSS, so a pre-rounded icon will look wrong.
   - **Screenshot** — `assets/<slug>.png`, set `image:`. This appears on the
     project page only. Portrait phone screenshots look right.
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
| `icon` | no | Filename in `assets/icons/`. Shown on the index card. Falls back to a monogram tile of the first letter. |
| `image` | no | Screenshot filename in `assets/`. Shown on the project page, not the index. |
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

## Keeping status honest

Hand-written statuses go stale the moment Apple approves something. Before
touching this repo, run:

```bash
python3 check_status.py
```

It asks the App Store what is actually published under the developer account and
reports anything that disagrees with `content/*.md` — an app marked in review
that has shipped, an app marked Live that is not there, or a published app with
no content file at all. It exits non-zero when something disagrees.

When it flags an app as newly live: set `status: Live` and add an
`App Store | https://apps.apple.com/us/app/<slug>/id<trackId>` entry at the
front of `links`.

Two older apps under the same developer account (`2-Letter Sight Words`,
`The Ice Run`, both `com.aariz.*`) are unrelated to these projects and will
always be reported as unmatched. Ignore them.

## House style for the prose

**The site is written in Zidaan's own voice — a middle schooler explaining his
own projects.** That is deliberate, not a placeholder. Match it exactly:

- **Plain words only.** No "leverage", "robust", "seamless", "architecture",
  "constraint", "deliberately". If a word would not turn up in a 6th-grade
  classroom, pick a different one.
- **Grammar stays correct.** Simple vocabulary, but no sentence fragments, no
  run-ons, no "me and my friend". The writing is easy, not sloppy.
- **First person.** "I built", "I figured out", "my first version". This is his
  portfolio, not a company's.
- **Short sentences**, and short paragraphs. Break a long one in two.
- Open with what the thing does and who would use it.
- The **tricky part** section is the point of each page: the thing that was
  actually hard. Explain it the way you would to a friend who does not code —
  concrete comparisons ("about the size of a pencil eraser") beat technical
  terms. Keep the real substance; only the vocabulary gets simpler. If nothing
  was hard, leave the section out.
- It is fine to admit things went wrong ("my first version was really annoying
  to play"). That reads as honest, and it is more interesting than a feature
  list.

This voice applies to `content/*.md` and the strings in `build.py` that end up
on the page. It does **not** apply to this file, `README.md`, or code comments —
those are notes for whoever maintains the repo, so keep them plain and direct.

## Related

The per-app marketing sites (`../warranty-site`, `../streak-site` and so on) are
separate repositories with their own privacy and support pages, which the App
Store requires. This portfolio links to them; it does not replace them.
