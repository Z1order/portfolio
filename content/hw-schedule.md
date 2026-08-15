title: HW Schedule
kind: Apple app
status: Ready to submit
order: 6
tagline: An eight-day school rotation, answered before you finish asking.
platforms: iPhone, Apple Watch
stack: SwiftUI, Vision
image: hw-schedule.png
links: Site | https://z1order.github.io/hwschedule-site/
---

Harvard-Westlake runs an eight-day, five-block rotation, which makes "what do I
have next?" a harder question than it should be. Open the app and the answer is
already on screen: the day of the cycle, the class running now with a bar
draining toward the bell, and what comes after it. Lift your wrist and you get
the same two answers without taking your phone out.

## What it does

- **Today**, with the current class and the next one.
- **The full rotation**, generated rather than typed in.
- **Scan a printed schedule** with the camera instead of entering eight classes
  by hand.
- **On the watch**, the same two answers at a glance.

## Worth knowing

The printed schedule looks like forty separate cells, but it is one continuous
rotation of eight lettered blocks, five per day, wrapping around. Day *n* opens
on block `5(n−1) mod 8`, and after eight days the cycle has used forty slots —
five whole trips through the eight letters — and lands back on A.

So the app stores **eight** facts, not forty. Change Block C once and it changes
on all five days it meets.

The scanner reads both the course list and the day grid, because they know
different things, and it leans on a useful redundancy: every block is printed
five times, once per day it meets. The parser collects all five readings of each
letter and takes the one most of them agree on, so a smudge or a bad line break
loses the vote instead of winning silently. The review screen shows the vote
count per block, and flags any block the photo only supports once.
