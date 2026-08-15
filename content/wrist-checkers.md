title: Wrist Checkers
kind: Apple app
status: Live
order: 7
tagline: Checkers on your watch, with taps that actually land where you meant.
platforms: Apple Watch (standalone)
stack: SwiftUI, watchOS
icon: wrist-checkers.png
image: wrist-checkers.png
links: App Store | https://apps.apple.com/us/app/wrist-checkers/id6797733559 ; Site | https://z1order.github.io/wrist-checkers/
---

Checkers on your Apple Watch against a computer opponent. You just tap the board
to move. You do not need your phone at all — the watch app is the whole game.

## What it does

- **Real checkers rules.** If you can jump, you have to jump. A chain of jumps
  counts as one move. Getting a king ends your turn.
- **Tap to move.** You tap out a double jump one hop at a time, like you would
  on a real board, but it saves as one move — so undo takes back the whole thing
  instead of leaving you halfway.
- **A computer to play against**, right on the watch, with no internet.

## The tricky part

A square on this board is about the size of a pencil eraser. That is way smaller
than what you are supposed to make a button, and my first version was really
annoying to play. The normal fixes are to shrink the board or make you confirm
every move, and both of those make the game worse.

What I did instead: when you tap, the app finds the closest square that you are
actually allowed to move to right now, and uses that one. This works because in
checkers you almost never have many choices. Before you pick up a piece, only
pieces that can move count. After you pick one up, only the squares it can reach
count. Since it is only checking against a few squares instead of all 64, each
one gets a much bigger invisible target around it. You can miss by a good amount
and it still does what you wanted.

There was also a weird problem that had nothing to do with the game. Apple gives
you no way to send a watch-only app to the App Store by itself. You have to hide
it inside an iPhone app that nobody ever sees or opens. If you try to send just
the watch app, there is no option for it anywhere.
