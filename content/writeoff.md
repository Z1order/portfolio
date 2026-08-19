title: Writeoff
kind: Apple app
status: Ready to submit
order: 23
tagline: Logs what you spend for work, so tax time is a CSV instead of a shoebox.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: writeoff.png
image: writeoff.png
links: Site | https://z1order.github.io/writeoff-site/
---

Writeoff is for anyone who has to keep track of business spending for taxes.
The idea is simple: you buy something, you log it in about fifteen seconds,
and in April you hand over one file instead of a shoebox full of paper
receipts.

## What it does

- **A threshold you set** — $75 by default — above which the app flags a
  purchase as needing a receipt photo, and keeps a running count of what's
  still missing.
- **Real tax categories**, matching the actual sections on a US tax form, so
  nothing needs re-sorting later.
- **Two separate numbers**: what you spent, and what you can actually claim.
  A work lunch might only be half deductible, and the app tracks that split
  instead of pretending every dollar counts the same.
- **Receipt photos**, attached right to the purchase.
- **A CSV and a written summary**, ready to hand off or paste into an email.

It's a record-keeping tool, not a tax advisor — it doesn't file anything for
you, and the category names are reminders, not official rulings.

## The tricky part

Money math has to be exact, and computers are secretly bad at exact decimals
unless you're careful. If you add up cents the ordinary way a computer wants
to, tiny rounding errors sneak in, and by the end of a year of receipts your
total is off by a few cents in a way nobody can explain. So every dollar
figure in this app uses a type built specifically for exact decimal money
instead of ordinary numbers. I even wrote a test that adds ten cents together
365 times and checks it comes out to exactly $36.50 — not $36.49999996 or
anything close to it.
