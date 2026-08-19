title: Shagun
kind: Apple app
status: In development
order: 28
tagline: A ledger for the cash-gift tradition at Indian weddings, so nobody forgets who gave what.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: shagun.png
---

At Indian weddings and other big family events, people give cash in
envelopes — it's called shagun. Someone always writes down who gave what,
and that notebook goes in a drawer for years, until it matters again the day
that family's own kid gets married. Shagun turns that notebook into an app.

The most important decision I made was building it around families, not
events. You write things down at one event, but you look things up years
later, and the question is always the same shape: this family's daughter is
getting married — what did they give at our event? So every family gets
their own page, showing everything given and received with them, across
every event, oldest to newest.

## What it does

- **A page per family**, with their full history and photos of the actual
  envelopes.
- **Fast entry during an event.** Pick the event once, then it's just name,
  amount, next — over and over without ever leaving the screen. Typing a new
  family's name creates them on the spot.
- **Quick amount buttons** for the traditional numbers, since these gifts
  almost always end in a 1 — like ₹501 or ₹1,100 — and typing that out by
  hand four hundred times in one evening would be miserable.
- **Two currencies, kept separate.** Families spread across countries often
  give in different currencies, and the app never mixes or converts between
  them, since there's no honest exchange rate for money given years ago.
- **PDF export**, so a family's page can be printed or emailed, not just
  looked at on one phone.

## The tricky part

Names were harder than I expected. A lot of the names in this app are in
scripts and spelling systems that don't work like English names, and I
needed to match "the same name typed two different ways" without matching
"two different names that happen to look similar." Some marks above or below
a letter genuinely change the word — like whether it's actually a different
vowel — and stripping those away would quietly merge two real families into
one page. Other marks are basically decorative and get left off half the
time by whoever's writing. I had to learn which was which for each script the
app supports, and I wrote tests that check both directions: strip the marks
that don't matter, but never the ones that do.
