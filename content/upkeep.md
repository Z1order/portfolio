title: Upkeep
kind: Apple app
status: In development
order: 10
tagline: A record of every repair you have ever done on a house, so you can look it up years later.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
icon: upkeep.png
---

Upkeep is a list of everything that has been fixed in a house. When you get the
boiler serviced or the roof patched, you write down what it was, when it was,
who did it, and what it cost. Then two years later, when it breaks again, you
can actually look up what happened last time.

It is mostly a notebook for stuff that is already done, not a to-do list —
with one exception: you can mark a job as needing doing again after a certain
number of months, and it will actually remind you.

## What it does

- **One log for each place**, so your house and a rented flat and your
  grandmother's apartment each keep their own history.
- **What you paid**, added up for the year, and split up by what kind of job it
  was.
- **The guarantee.** If the work came with one, the app shows a green mark on
  it while it is still good. That is really the whole reason to write the
  guarantee down.
- **A reminder for the jobs that repeat.** Mark a fix as due again in so many
  months, and the app tells you on the day, then logs it as a fresh entry
  prefilled from the last one when you do it — so the history stays a list of
  what actually happened, not a schedule of what's supposed to.
- **Photos and a phone number** for whoever did the work, so you can call the
  same person again.
- **Search**, across the job, the room, the person, and your notes.

## The tricky part

Money turned out to be harder than I expected.

The first version just stored a number. That works until you have receipts from
two different countries, which happens the second somebody keeps a log for a
place they used to live in.

I could have converted everything into one currency, but there is no honest way
to do that. A repair paid for in 2019 was paid at the 2019 rate, and nobody
knows what that was anymore. If I picked today's rate, the app would show a
total that looks exact and is quietly wrong. That is worse than not showing one.

So every cost remembers the money it was paid in. If a log has more than one
kind of money in it, the app says so underneath the total instead of pretending
it can add them together.
