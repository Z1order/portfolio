title: Gully
kind: Apple app
status: In development
order: 29
tagline: A cricket scorer built for the backyard game, not the TV broadcast.
platforms: iPhone, Apple Watch
stack: SwiftUI, SwiftData, WatchConnectivity
icon: gully.png
---

Gully is a cricket scorer for the casual park version of the game — five
overs, eight a side, last man batting alone, and someone's cousin still
parking the car. The whole app is built around one rule: recording a ball has
to take under three seconds and survive being done wrong, because the person
scoring would rather be watching the game, and they will absolutely tap the
wrong button while the next ball is already being bowled.

## What it does

- **A big grid of one-tap buttons** for the score — 0, 1, 2, 3, 4, 6 — plus
  wide, no ball, and wicket, all one tap each.
- **Unlimited undo**, always correct. Since nothing is stored except the list
  of balls bowled, undoing just removes the last one and everything else —
  the score, the over, whose turn it is to bat — fixes itself automatically.
- **House rules you actually argue about**, chosen before the match: how many
  overs, whether last man bats alone, whether LBW is even being called.
- **Score from the watch**, for whoever's fielding and doesn't want to touch
  their phone mid-over.

## The tricky part

The whole app works because nothing is stored except a plain list of what
happened, ball by ball — no running score, no separate "who's batting" flag.
Every number on every screen gets recalculated from that list every single
time you look at it. That sounds slow, but a whole five-over match is only
about sixty balls, so redoing all the math from scratch is instant.

That one decision is also what makes undo trustworthy. Undo just deletes the
last ball from the list and recalculates — there's no separate score sitting
around that could disagree with the list of balls. And it's what makes
syncing between the phone and the watch simple, too: two lists of balls can
just be combined into one, in any order, without needing a server to decide
whose version is right.
