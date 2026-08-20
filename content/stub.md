title: Stub
kind: Apple app
status: Ready to submit
order: 21
tagline: Tells you the exact minute leaving a parking garage will cost you more money.
platforms: iPhone
stack: SwiftUI, SwiftData, ActivityKit, CoreLocation
icon: stub.png
image: stub.png
links: Site | https://z1order.github.io/stub-site/
---

Parking garages charge in steps. $8 for the first hour, $16 up to two hours,
$24 up to three, and so on — and the rate board at the entrance is the last
time you ever see those numbers again. Stub answers one question, live, right
on your lock screen: is leaving right now about to cost me more, or have I
already paid for the time I'm using?

## What it does

- **Save a spot once**, typing in the rate board's steps and daily max.
  Around six garages covers most people's whole life, so it's fine that this
  part takes a minute.
- **A live lock screen card** showing what you owe right now and a countdown
  to the next price jump, in a color that changes when you're close to one.
- **A notification before every jump**, like "next step in 10 minutes —
  leave now and save $8," so you don't have to keep checking.
- **Tells you when you've already paid for the rest of the hour**, too — so
  you stop sprinting back to a car you don't need to sprint back to.
- **Works for meters too**, just flipped around: you already paid, so it
  counts down to when your time runs out instead.

## The tricky part

A parking garage's price is not one smooth line going up — it jumps at
specific moments, resets every midnight, and sometimes switches to a flat
evening rate that can honestly cost more for a short stay than the same stay
at noon would have. I had to write one function that all of this math goes
through, so the lock screen card and the notifications can never disagree
about what you owe.

The other annoying part was the lock screen itself. I found out that a live
countdown timer on the actual lock screen doesn't count seconds — it just
shows a dash and only updates once a minute, even though the exact same kind
of timer counts every second in the Dynamic Island, the pill shape at the top
of the screen. So instead of fighting that, I show a fixed deadline on the
lock screen — the exact time you need to be out by, which never goes stale —
and I save the live ticking countdown for the place that can actually show
it.
