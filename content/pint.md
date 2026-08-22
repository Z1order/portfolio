title: Pint
kind: Apple app
status: In development
order: 44
tagline: Tells a blood donor exactly when they can donate again, for each type of donation.
platforms: iPhone, Apple Watch
stack: SwiftUI, SwiftData, WatchConnectivity
icon: pint.png
---

Pint is for people who give blood. After you donate, you have to wait before
you can donate again, but the wait is different depending on what you gave and
what you want to give next. A whole blood donation blocks you from giving
whole blood again for 56 days, but only blocks platelets for 7. Nobody keeps
all of that in their head, so Pint keeps a log of every donation and tells you
exactly what you can give today, and when the rest open back up.

## What it does

- **One row per donation type**, each one either open now or counting down to
  the day it opens, with the reason spelled out in words instead of just a
  date.
- **Logging takes one tap.** The date defaults to today, but you can enter an
  old donation from memory too, which is usually the first thing a new user
  does.
- **One notification per type**, sent the day it reopens. Nothing repeats and
  nothing nags.
- **A widget and a watch complication** that just show the days left, since
  this is an app people glance at more than open.
- **A lifetime count**, with total volume given and quiet notes at donation
  10, 25, 50, and so on.
- **Rules for the US, India, and the UK**, since the wait times and yearly
  limits are different in each place.

Pint only tracks the waiting rules. It does not ask health questions or decide
if you are allowed to donate — that is always up to the blood center.

## The tricky part

The rules are not just one number per donation type. Every type of donation
blocks every other type by a different amount, so there is really a whole grid
of numbers, not a list. Missing even one square in that grid is dangerous in
one specific direction: an empty square would quietly mean "no wait at all,"
which is the wrong way to fail. So there is a test that fails the build itself
if any square in the grid is left blank.

The other tricky part was getting the watch and the phone to agree on the log
without a server in between. The phone is treated as the one true copy, and
sends the watch a full copy of the log whenever they connect. The watch is
only ever allowed to add new donations, kept in a small waiting list until the
phone's next copy shows it received them. That one rule, that the watch can
only add and never change or delete, is what let me skip writing any code to
resolve a conflict between them.
