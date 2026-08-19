title: Mancala
kind: Apple app
status: Ready to submit
order: 33
tagline: Mancala for Apple Watch, against a real opponent or pass-and-play.
platforms: Apple Watch (standalone)
stack: SwiftUI, watchOS
icon: mancala.png
image: mancala.png
links: Site | https://z1order.github.io/mancala-site/
---

Mancala is the classic pit-and-stone game, built for the Apple Watch screen.
Play against the watch or pass it back and forth with a friend. The board is
turned to fit the watch's shape, so your stones travel down one side and back
up the other, into your own store.

## What it does

- **Tap a pit** to scoop up its stones and drop one in each pit going
  around the board, the normal rules of Mancala.
- **Land your last stone in your own store and you get another turn** — the
  rule that makes the game more about planning ahead than luck.
- **Play against the watch itself**, which thinks several moves ahead instead
  of just picking randomly.

## The tricky part

The watch has no menu button like the iPhone does — that control simply
doesn't exist on watchOS. So for the options screen, where you'd normally tap
a menu, I had the toolbar button open a full sheet instead. It's a small
difference, but it's the kind of thing you only find out by actually trying
to build the screen you had planned and discovering the button you wanted
isn't available on this platform at all.
