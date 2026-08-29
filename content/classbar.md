title: ClassBar
kind: Apple app
status: In development
order: 53
tagline: A floating card on my Mac that shows my whole school day and what class I have next.
platforms: Mac
stack: Swift, SwiftUI, AppKit, WebKit
---

ClassBar sits on top of everything on my Mac and shows my school day in order —
every class, when it starts, which teacher and which room. I made it because I
was checking two different school websites every morning to answer one question,
which is what class do I have next.

## What it does

- **The whole day, in order.** Each class with its time, its block letter, the
  teacher and the room. Lunch, advisory and clubs are in there too, wherever the
  school actually put them that day.
- **Marks the class I am in right now**, and the one right after it.
- **Switches to tomorrow on its own.** Once the last class of the day is over,
  the card shows the next school day instead. So looking at it after dinner
  tells me what to pack, and looking at it in the morning tells me what I have.
- **Arrows at the bottom look further ahead**, one school day at a time. They
  skip weekends and holidays, so there is never an empty day to page past. A
  **Now** button jumps back to today, and it goes back by itself after a couple
  of minutes if I forget.
- **Shrinks into a small bubble** with the rotation day in it, and comes back
  with a keyboard shortcut.

## The tricky part

Nothing my school gives me knows my whole schedule. Two different websites each
know half of it.

The schedule page knows **when**. It has every date of the year, which day of the
rotation it is, and the real bell times — including all the strange days, like
the late starts and the assembly days and the first day where every class meets
for fifteen minutes. I could not have worked those out from a pattern. They just
have to be read.

The class website knows **what**. It has my eight classes and my teachers on it.
But it has no calendar at all, so it never says when any of them meet. The only
place that shows up is inside the name of each class, which looks like this:
`x.F.F.x.F.F.x.F`. Eight spots for the eight days of the rotation, and the letter
is the block. Once I noticed that, the two halves clicked together. The schedule
page says "Block F at 10:35" and the class website says Block F is English.

Then there was the part where the school's site would not answer me at all. It
sits behind one of those "checking your browser" screens, and anything that is
not a real browser gets turned away. My app was not a real browser, so it kept
getting the door shut on it. What works is opening the page in a hidden window
first and letting that screen run its check, then asking for the file from inside
that window, where it counts as a browser and gets let through.
