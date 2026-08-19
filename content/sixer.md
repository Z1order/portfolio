title: Sixer
kind: Apple app
status: In development
order: 32
tagline: A cricket batting game for Apple Watch, where your timing decides the shot.
platforms: Apple Watch (standalone)
stack: SwiftUI, watchOS
icon: sixer.png
---

Sixer is a one-handed cricket game for Apple Watch. You bat, the watch
bowls, and you pick a shot with the Digital Crown before each ball arrives.
One tap plays it, and how close that tap lands to the ball actually reaching
you decides whether you get a six, a dot ball, or get out.

## What it does

- **Four shots** — block, push, drive, loft — each safer or riskier than the
  last. A block barely scores but almost never gets you out; a loft can go
  for six but usually doesn't.
- **Two ways to play.** Chase a target that grows every time you reach it, or
  bat in the nets until you're out three times and try to beat your best
  score.
- **The length of the ball changes the risk** — a short ball rewards a big
  shot, a full one punishes you for swinging too hard.

## The tricky part

The whole game depends on exact timing, and I found out the normal way apps
detect a tap on the watch — a tap gesture — only actually fires the instant
you lift your finger, not the instant you touch down. For a timing-based game
that's a real problem, because it means every shot would register a tenth of
a second later than when you actually meant to hit the ball. I had to switch
to a lower-level kind of touch detection that fires the moment your finger
lands instead, so the timing in the game matches the timing you actually feel.
