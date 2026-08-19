title: Tare
kind: Apple app
status: Ready to submit
order: 22
tagline: A weight tracker that shows you the real trend, not the noise.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: tare.png
image: tare.png
links: Site | https://z1order.github.io/tare-site/
---

Your weight bounces around by a kilo or more from one day to the next, just
from water and food, so the number on the scale by itself doesn't tell you
much. Tare has you log what the scale says, but every important number it
shows you — the big number at the top, how much you've changed this week,
how fast you're going, your projected goal date — is worked out from a
smoothed line running underneath the bouncing, not from today's single
reading.

## What it does

- **Log a reading** in kilograms, pounds or stones, in about two taps.
- **A trend line**, not just a dot-to-dot chart. The raw readings are still
  there, drawn as faint dots, so you can see how much noise the trend is
  cutting through.
- **A goal**, with a progress bar and a projected date based on how you've
  actually been moving over the last few weeks — not shown at all if you're
  currently heading away from your goal, because a wrong projection is worse
  than no projection.
- **History** by month, with each entry showing how much it changed from the
  last one.
- **CSV export**, if you ever want your data somewhere else.

Weight is always stored in kilograms behind the scenes and only converted for
display, so switching units never rewrites your history. And the app colors
a change based on your actual goal, not just whether the number went up —
because if you're trying to gain weight, a bigger number is a good day, not a
red one.

## The tricky part

The whole point of this app is the trend line, so I had to actually build a
formula that turns bouncy daily numbers into a smooth one. It's a kind of
moving average that leans more on recent readings than old ones, and it also
has to handle gaps — if you don't weigh in for two weeks, it shouldn't let
one old stale number keep dragging the trend around after you start again.
Getting that balance right, so the line reacts to real changes but doesn't
jump around on noise, took a lot of tweaking with real data before it felt
right.
