title: Warranty
kind: Apple app
status: Ready to submit
order: 2
tagline: Keeps the receipt, and tells you before the cover runs out.
platforms: iPhone, iPad (iOS 17+)
stack: SwiftUI, SwiftData, CloudKit, Vision
icon: warranty.png
image: warranty.png
links: Site | https://z1order.github.io/warranty-site/
---

You buy a dishwasher. Two years later it stops draining, the warranty had
eleven months left, and the receipt went in the bin. Warranty exists for that
afternoon. Photograph the receipt at purchase, and the app tells you a month
before the cover lapses — while there is still something you can do about it.

## What it does

- **Scan the receipt, not the form.** Point the camera at it and the shop, the
  date and the total arrive already filled in, ready to correct.
- **A countdown, not a date.** "Expires in 3 months" reads faster than a date
  in 2027. Under a month turns red; expired items fold away.
- **One notification per item**, thirty days out by default. That is the only
  alert the app will ever send.
- **A PDF for the shop.** One page: what it is, where and when you bought it,
  what it cost, with the receipt photo attached.

## Worth knowing

Vision returns one observation per *run* of text, not per line. On a real
receipt that means `TOTAL` and `470.38` come back as two separate results, and
so do a date and the time printed beside it.

Feed that straight to a parser and the rule "the total is the largest amount on
a line saying total" matches nothing at all — it falls through silently to
"largest amount anywhere" — while a bare `14:32` gets read as a date and
resolved to today. So observations are grouped back into printed lines by
vertical position before the parser ever sees them. The live scanner and the
still-photo fallback both go through that same step, which is why they cannot
drift apart.
