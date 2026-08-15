title: Conjugar
kind: Apple app
status: Ready to submit
order: 5
tagline: Spanish verb drills that compute the answer rather than look it up.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
image: conjugar.png
links: Site | https://z1order.github.io/conjugar-site/
---

Drill any of 116 verbs across 11 tenses, or look up a full conjugation table.
Spaced repetition schedules what comes back and when, starting at two minutes so
a mistake can be corrected inside the same sitting.

## What it does

- **Drill mode** over any subset of verbs and tenses.
- **Reference tables** for the whole conjugation of any verb.
- **Progress** per verb and tense, so you can see what is not sticking.

## Worth knowing

Conjugation is computed, not stored. Regular endings, stem changes,
orthographic repairs and the strong-preterite family are all derived, and a verb
carries an explicit override only where Spanish genuinely stops being
systematic — `ser`, `estar`, `ir`, `haber`, `dar`, `ver`, `oír`, `saber`.

Tenses lean on each other the way a grammar book does. The present subjunctive
is built from the `yo` present, the imperative from the present subjunctive, and
the imperfect subjunctive from the third-person plural preterite. Each rule is
written once, so an irregularity propagates for free: `decir` → `dijeron` →
`dijera` needs no extra data at all.

The rule that earns its keep is that an irregular `yo` form beats stem reversion
outside the boot. That single fact is what separates `tengamos` and `vengamos`
from the wrong `tenamos` and `vinamos`, and `sigamos` from `siguamos`.

Progress is stored as one running tally per verb and tense, with deliberately no
per-answer log. The store stays bounded at around 1,270 rows instead of growing
with every answer forever.
