title: Box
kind: Apple app
status: In development
order: 43
tagline: Keeps track of which moving box has what in it, so you can find it later.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: box.png
---

Box is for moving house. Writing "KITCHEN" on the side of a box tells the
movers where to drop it, but it does not tell you which of nine identical
boxes has the kettle in it four days later. Box answers that question. Search
"kettle," and it tells you it's in box 14, still on the van.

## What it does

- **A fast way to pack.** Start a new box, type what's going in it while you
  pack, and the number is already assigned. Under thirty seconds a box, one
  handed.
- **A photo of the open box** before you tape it shut, so you have a record of
  everything you didn't bother to type.
- **A printable label for every box**, with the number huge, the room it's
  going to, and a QR code you can scan to open that box's page from your
  phone.
- **Search from anywhere in the app**, across every item, room, and box
  number.
- **A loading checklist** that says exactly how many boxes are loaded, so a
  missing box turns up while the movers are still there.
- **Nothing gets deleted when the move is done.** The whole list sticks
  around, ready for the next move.

## The tricky part

Two boxes can never end up with the same number, even years apart. If box 14
from a move in 2024 and box 14 from a move next year both mean something, the
QR code on the label is useless — scanning it would not know which box you
actually mean. So every move keeps its own running count that only ever goes
up, and deleting a box never hands its number to a different box later. The
only time a number goes back into the pool is if you back out of a box you
just started and never put anything in it.

The QR code itself had to carry the move along with the box number, not just
the box number by itself, for the same reason. So the code is really a link,
like a web address, with the move and the box both built into it. A code that
merely looks like one of the app's own opens nothing at all, rather than
guessing and opening the wrong box.
