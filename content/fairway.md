title: Fairway
kind: Apple app
status: Live
order: 9
tagline: Keep score for a round of golf and watch everyone else's scores come in live.
platforms: iPhone (iOS 17+)
stack: SwiftUI, SwiftData, CloudKit
icon: fairway.png
image: fairway.png
links: App Store | https://apps.apple.com/us/app/fairway-live-golf-scoring/id6802113639; Site | https://z1order.github.io/fairway-site/
---

Fairway is for keeping score while you play golf with other people. You look up
the real course by name, share a six letter code with your group, and everyone's
scores show up on one leaderboard as they type them in.

There is no sign up. No email, no password, no account. The first time you open
it, it asks your name, and that is the whole setup.

## What it does

- **Real courses.** Over 32,000 of them, with the par and the difficulty of
  every hole already filled in.
- **A live leaderboard** that updates while you are still playing.
- **Lots of ways to score**, not just adding up strokes. Match play, Stableford,
  skins, and team games.
- **Handicaps done right**, so a beginner and a good player can actually have a
  close game.
- **Type in your own course** if it is not in the list, which happens a lot
  outside the United States.

## The tricky part

Golf does not happen all at once. Your group is on the 7th hole and the group
behind you is on the 3rd, and both of you are typing into the same leaderboard.

The obvious way to build it is to add up every hole everybody has played. That
is completely wrong. Someone who has played nine holes badly still looks like
they are beating someone who has only played three, just because they have more
holes on the board. And the whole thing jumps around every time the slower group
catches up.

So the leaderboard only compares holes that both players have actually
finished. If you are on the 12th and I am on the 3rd, we are only being compared
over three holes. Every row on the screen also says how many holes that person
has played, so you can see for yourself.

Skins have the same problem in a sneakier way. A skin goes to whoever wins the
hole outright. But two people tied on a 4 is not a tie if somebody in the group
is still standing over a putt for 3. So a hole cannot be settled at all until
everyone has played it.

The other hard part was making it feel instant without trusting it to be. When
someone posts a score, Apple sends a little silent message to everyone else's
phone. That works great, except a golf course is exactly the sort of place with
bad signal, and those messages get dropped all the time. So the app also just
asks the server for new scores every twelve seconds. The message is what makes
it feel fast. The asking is what makes it right.
