title: Warranty
kind: Apple app
status: Ready to submit
order: 2
tagline: Saves your receipts and warns you before a warranty runs out.
platforms: iPhone, iPad (iOS 17+)
stack: SwiftUI, SwiftData, CloudKit, Vision
icon: warranty.png
image: warranty.png
links: Site | https://z1order.github.io/warranty-site/
---

Say you buy a dishwasher. Two years later it breaks, and it turns out the
warranty still had eleven months left on it — but the receipt got thrown away a
long time ago, so you cannot prove anything. That is the whole reason this app
exists. You take a picture of the receipt when you buy something, and the app
tells you a month before the warranty ends, while you can still do something
about it.

## What it does

- **Take a picture instead of typing.** Point the camera at the receipt and the
  store, the date, and the price show up already filled in. You just fix
  anything it got wrong.
- **It counts down.** "Ends in 3 months" is way easier to understand than a date
  in 2027. Less than a month left turns red, and expired stuff hides itself.
- **One reminder per item**, thirty days before the warranty ends. That is the
  only notification the app will ever send you.
- **A PDF to bring to the store.** One page with what you bought, where, when,
  how much it cost, and a picture of the receipt.

## The tricky part

The part of the phone that reads text does not hand you whole lines. It hands
you little chunks. So on a real receipt, the word `TOTAL` comes back as one
chunk and `470.38` comes back as a completely separate one, even though they are
printed right next to each other.

That breaks everything. My rule was "the total is the biggest number on a line
that says total," but if `TOTAL` and the number are never on the same line, that
rule never matches anything. Worse, it fails quietly instead of telling you, so
it just grabs the biggest number anywhere on the receipt. And a time like
`14:32` gets read as a date, which the phone helpfully decides means today.

So before anything else happens, I put the chunks back into lines by looking at
how high up the page each one is. Chunks at the same height belong to the same
line. Both the live camera and the take-a-photo version use that same code, so
they can never disagree with each other.
