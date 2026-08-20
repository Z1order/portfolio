title: Awake
kind: Apple app
status: In development
order: 36
tagline: A clock for the people you call across time zones, so you know when it's actually okay to call.
platforms: iPhone, home screen widget
stack: SwiftUI, SwiftData, WidgetKit
icon: awake.png
image: awake.png
links: Site | https://z1order.github.io/awake-site/
---

If you have family or friends far away, you know the problem: is it too late
to call them right now? Figuring that out takes doing math in your head, and
that little bit of math is annoying enough that people just don't call.
Awake does the math for you and tells you the answer straight up: good time
to call, just up, or asleep, don't.

## What it does

- **A list of people**, sorted so whoever you can actually call right now is
  at the top, each one shown in a color for good, just up, or asleep.
- **A day bar for each person**, showing their waking hours lined up against
  yours, so you can see exactly when your days overlap.
- **A widget** for your home screen that tells you the good part without you
  even opening the app: "good until 11:30 AM your time."

## The tricky part

The hard part wasn't the clocks, it was the widget. A widget can't run code
whenever it feels like it — you have to hand it a list of times ahead of
time and say "draw this at this moment, and this other thing at that
moment." So I had to figure out, in advance, every single moment a person's
status could change: when they wake up, when they go from "just up" to
regular awake, when they go to bed, plus every midnight in every time zone
involved, plus daylight saving changes.

Daylight saving was the part that actually broke my first version. On the
day clocks change, an hour either gets skipped or repeated, so a window like
"awake from 8am to 10pm" can end up 23 hours long or 25 hours long that one
day. I had to test both of those days in multiple time zones to make sure
nobody's status flickered on and off at the wrong moment.
