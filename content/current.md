title: Current
kind: Apple app
status: Ready to submit
order: 18
tagline: Tracks how close you are to a green card, and tells you if the line moved this month.
platforms: iPhone
stack: SwiftUI, SwiftData, WidgetKit
icon: current.png
links: Site | https://z1order.github.io/current-site/
---

Once a month the government publishes a bulletin that tells certain immigrants
how close they are to getting a green card. It is a giant confusing table on an
old government website, and people who are waiting check it every single
month for years. Current reads that table for you and answers one question:
did my line move, and how far do I have left?

## What it does

- **How far you have left**, in years and months, not some date you have to do
  math on yourself.
- **What changed this month**, in plain words. Moved forward, stayed the same,
  or even moved backward — that happens, and the app says so honestly instead
  of hiding it.
- **A chart** of your line over sixteen years, so you can actually see the
  shape of the wait instead of one number a month.
- **A widget** on your home screen or lock screen, since most months you just
  want a glance, not the whole app.
- **A notification** that tells you the actual answer — "moved forward 1
  month, 2 years 4 months to go" — instead of just "a new bulletin is out,"
  which tells you nothing.

## The tricky part

The government publishes this table as a web page, and the page has changed
its shape a bunch of times over the last sixteen years. Old pages use
different words for the same thing, add new rows, and split old rows into new
ones. My app has to read all of them correctly, not just the newest one,
because it builds its whole sixteen-year history from real saved copies of
every shape the page has ever had.

The sneakiest bug was about dates. The government's own web address for a
bulletin uses next year's number for the last three months of this year,
because their calendar starts in October. I did not know that when I started,
so my first version worked fine nine months of the year and quietly broke for
October, November and December — which is exactly long enough for a bug like
that to ship without anyone noticing.

The other rule I hold myself to: if the app cannot read a page cleanly, it
never guesses. It just says "couldn't read this month's bulletin" and shows
you the last one that worked. Showing someone the wrong number here is worse
than showing them an old one, because a wrong number could tell somebody
their line moved when it didn't.
