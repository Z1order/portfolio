title: Conjugar
kind: Apple app
status: Ready to submit
order: 5
tagline: Spanish verb practice that figures out the answer instead of storing it.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
icon: conjugar.png
image: conjugar.png
links: Site | https://z1order.github.io/conjugar-site/
---

Practice any of 116 Spanish verbs in 11 different tenses, or just look up a
whole verb chart. The app brings back the ones you keep missing, and it starts
by asking again after only two minutes, so you can fix a mistake while you are
still sitting there.

## What it does

- **Practice mode** with whatever verbs and tenses you want.
- **Charts** for any verb, if you just need to look something up.
- **Progress** for each verb and tense, so you can see what is not sticking.

## Why I built it this way

The app does not have a giant list of every verb form typed out. It works them
out from rules instead. Regular endings, verbs that change in the middle,
spelling fixes, and the weird past-tense group are all figured out. A verb only
gets its answers written out by hand when Spanish stops following any pattern at
all, which is really only eight verbs: `ser`, `estar`, `ir`, `haber`, `dar`,
`ver`, `oír`, and `saber`.

The cool part is that the tenses are built out of each other, the same way your
Spanish textbook teaches them. The present subjunctive comes from the `yo` form.
The commands come from the present subjunctive. The past subjunctive comes from
the `ellos` preterite.

That means I only write each rule once, and weird verbs stay weird all the way
down without me doing anything. `decir` turns into `dijeron`, which turns into
`dijera`, and I never had to type in `dijera` anywhere.

For saving your progress, I only keep a running score for each verb and tense —
not a record of every single answer. That keeps it at about 1,270 rows no matter
what, instead of growing forever the longer you use the app.
