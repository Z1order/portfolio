title: Haazri
kind: Apple app
status: In development
order: 40
tagline: A work diary for people who work at several houses, so they always know how many days they came and for how long.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: haazri.png
---

Haazri is for people who work at more than one house — a cook, a driver,
someone who cleans a few places a week. You tap once when you get to a house
and once when you leave, and at the end of the month it hands you a plain
summary of every house: how many days, how many hours, and what it comes to.

## What it does

- **One big button for arrive, one for leave**, at each house, in the order
  you actually walk them.
- **A second shift at the same house works fine** — the morning's hours stay
  on the card while the evening one runs.
- **Days off get a reason**, so "I took the day" and "the house said no
  work" don't get mixed up.
- **A month summary in plain text**, ready to send, that shows every house
  at once.

## The tricky part

The hardest part was deciding what to do about a shift nobody remembered to
close. Phones go in bags, and if the app just measured "leave time minus
arrive time," a forgotten shift from three days ago could say you worked
forty-eight hours straight.

So a shift left open on a past day counts zero hours instead of guessing —
the day still counts as worked, but the hours are just missing, and the app
asks you to fill in a leaving time while you can still remember it. Making
up a number would have been easy and wrong; showing nothing felt honest.
