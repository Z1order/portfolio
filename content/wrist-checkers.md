title: Wrist Checkers
kind: Apple app
status: Live
order: 7
tagline: English draughts on a watch, with taps that land where you meant them.
platforms: Apple Watch (standalone)
stack: SwiftUI, watchOS
icon: wrist-checkers.png
image: wrist-checkers.png
links: App Store | https://apps.apple.com/us/app/wrist-checkers/id6797733559 ; Site | https://z1order.github.io/wrist-checkers/
---

A standalone Apple Watch draughts game against a built-in engine, played by
tapping the board. No phone required — the watch app is the whole app.

## What it does

- **English draughts**, properly: mandatory capture, chained jumps as one move,
  crowning ends the turn.
- **Tap to move.** Multi-jumps are tapped out one hop at a time, as on a
  physical board, and commit as a single move — so undo takes the whole chain.
- **An engine to play against**, on the watch, offline.

## Worth knowing

A square on this board is about 17pt across, which is well under a comfortable
tap target. The usual fixes are to shrink the board or add a confirmation step,
and both make the game worse.

Instead, taps snap to the nearest square that is **legal right now**. That works
because a checkers position offers very few real choices: before a piece is
picked up only pieces with a legal move are candidates, and afterwards only the
squares that piece can reach. Matching against that handful by proximity rather
than by exact bounds makes the effective targets several times larger than the
squares they sit on, so a tap that lands 15pt off-centre still does the right
thing.

The other constraint is structural. Xcode ships no watchOS App Store
distribution method — there are App Store methods for iOS, Mac, tvOS and
visionOS, but not for the watch. So a watch-only app reaches the store *inside*
an iOS stub app that users never see. You archive the iOS scheme; archiving the
watch app alone produces something that cannot be distributed at all.
