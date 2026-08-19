title: Ticklist
kind: Apple app
status: Live
order: 15
tagline: Checklists you can reset and reuse, instead of writing the same list every time.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
icon: ticklist.png
image: ticklist.png
links: App Store | https://apps.apple.com/us/app/ticklist-packing-lists/id6802302275; Site | https://z1order.github.io/ticklist-site/
---

Ticklist is for lists you use over and over: pack the bag, tick everything off,
clear the ticks, and the same list is ready for the next trip. I built it for
packing, but it works for anything with the same shape, like a gym bag or a
moving day.

## What it does

- **Lists that survive being finished.** Clearing the ticks keeps every item
  and remembers you got to the end. Duplicating a list gives you the same one
  minus the ski boots, for the trip where nobody skis.
- **Nine starter lists** already written for you: weekend away, beach,
  camping, business trip, day hike, gym bag, baby bag, festival, and moving
  day. The hardest part of a packing list is the first draft at 11pm the night
  before, so I wrote those already.
- **Headings you write yourself.** Type "Under canvas" or "Dog" and that
  becomes a heading. There is no separate screen to make one, and nothing to
  clean up later, either — a heading just exists for as long as something is
  under it.
- **A quick-add box that stays on screen.** Type "3 socks" and it adds three.
  Type something already on the list and it adds to that row instead of making
  a second one, and unticks it, since more of something means you are not
  packed yet.
- **One tap anywhere on a row** ticks it, and the row stays put instead of
  jumping to the bottom while you are still tapping the next thing.

## The tricky part

The quick-add box is the whole point of the app, so it had to do more than
just add a line. If your list already has a "Documents" heading and you type
"passport," it should land under Documents, not just get tacked onto the
bottom in a random spot.

So before adding anything, the app checks two things: is this already on the
list, and if it is new, does it sound like something that belongs under a
heading you already have. It never invents a new heading on its own, because
how someone sorts their own packing list is their call, not the app's. It only
ever offers to use headings you already typed yourself.

The other trick is what "add" means when the words already match something on
the list. Typing "socks" twice does not make two rows. It bumps the number on
the existing row and unticks it, because if you are adding more socks, the
socks you already packed are not the reason you are done packing.
