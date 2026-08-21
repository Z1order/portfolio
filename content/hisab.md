title: Hisab
kind: Apple app
status: In development
order: 41
tagline: A ledger for the people a household employs, so payday math is arithmetic instead of an argument.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: hisab.png
---

Hisab is for households that employ people — a cook, a driver, someone who
cleans. Nobody forgets the salary, but everybody forgets the small stuff:
the cash handed over on the 9th, or whether someone missed two days last
month or three. Hisab is built to catch those small things the second they
happen, so payday is just adding up numbers both people already agree on.

## What it does

- **Two buttons on the main screen**: mark someone absent today, or record
  an advance, both in one tap.
- **A settlement that shows its work.** Salary minus advances minus leave
  plus extras, one line at a time, and you can tap any line to leave it out
  of this month.
- **Salary history, not just a salary.** A raise is a new dated row, so the
  app can still answer what someone was paid a year ago.
- **A year statement as a PDF**, so household staff have something to show
  a landlord or a bank when they need to prove what they earn.

## The tricky part

The trickiest part was the math around a raise that happens in the middle
of a month. Everyone I asked said the same thing — "just divide the salary
by thirty" — so a day of leave always costs a thirtieth of the salary, even
in February. But when a raise lands on, say, the 16th, the days after that
are worth more than the days before it, and the app has to add those two
different daily rates together correctly instead of just picking one number
for the whole month. Getting that split right, and getting it to agree with
what people expect when they do the math in their head, took the most
tries.
