title: Postcard
kind: Apple app
status: In development
order: 13
tagline: Plan a trip day by day, then keep what you thought of every place after you go.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
icon: postcard.png
image: postcard.png
links: Site | https://z1order.github.io/postcard-site/
---

Postcard plans a trip as a list of places. You tick each one off while you are
there and write a line about what you thought of it. Nothing gets deleted when
you get home, so the next time you go to Japan, the app opens with what was
actually good last time.

The two halves need each other. A plan with no memory is just a checklist you
throw away after the trip. A travel journal with no plan is something nobody
ever fills in.

## What it does

- **A plan by day.** Every day of the trip gets its own spot, even the empty
  ones, because seeing the gaps is how you notice you have nothing planned for
  Tuesday.
- **Ideas.** Somewhere you want to go but have not put on a day yet. Drag it
  onto a day once you decide, or pull it back off if you change your mind.
- **A tick and a verdict.** Been or not been, then loved it, fine, or skip it
  next time. Three choices instead of five stars, because a year later the only
  thing you actually remember is whether you would send someone else there.
- **A line about it.** "Get there before 7am." That one sentence is the whole
  point of writing anything down.
- **The return trip.** Type a place you have already been and the new-trip form
  turns into a briefing of everywhere you loved there and what you wrote about
  it, ready to add straight onto the new plan.
- **A crowded-day warning.** More than four things on one day gets flagged, so
  you find out before you are standing in Kyoto at 4pm with three temples still
  to go.

## The tricky part

Say you go to Japan twice, two years apart. The app should know that is one
place you have been, not two, so the second trip gets advice from the first one
instead of starting blank.

The problem is what people actually type. "Japan", "japan", and "Japan " with a
space at the end are three different words to a computer, even though they mean
the same place to you. So before the app checks whether two visits are the same
place, it lowercases everything, trims the extra spaces, and strips out accents,
so "São Paulo" and "Sao Paulo" match too.

The other half is which verdict wins when the same place shows up twice. If you
loved a restaurant in 2024 and had an okay meal there in 2026, the app keeps
"loved it," not whichever visit happened most recently. A bad second visit
should not erase a good first one. Advice for a new trip also only ever comes
from trips that have already finished, so a trip you have not gone on yet can
never end up giving itself advice.
