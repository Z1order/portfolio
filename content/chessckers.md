title: Chessckers
kind: Game
status: Live
order: 1
tagline: A whole chess army versus 24 stacking checkers. Play it in your browser.
platforms: Web, desktop (Godot)
stack: Godot 4.7, C#, JavaScript
links: Play in your browser | https://z1order.github.io/chessckers/
---

**Chessckers** is a board game where one player gets a full chess set and the
other gets 24 checkers that can stack on top of each other. So the two sides are
not the same at all, which is what makes it fun.

I did not invent this game. It was made, written, and illustrated by M. Edden
Ishaaya and engineered by Nikita Ulianov. All I did was write a version you can
play on a computer, using the rules they published.

## What it does

- **Play in a browser.** Nothing to download and nothing to install. It is all
  one page.
- **Play by yourself** against a computer opponent in the browser version.
- **A desktop version** in Godot for two people on one screen.

## Why I built it this way

The part that knows the rules is completely separate from the part that draws
the game. That means I can test the rules without ever opening the game, which
saved me a huge amount of time.

The browser version is not an export of the desktop one. I wrote it a second
time from scratch, in a different language, and split it into three pieces: the
rules, the computer opponent, and the drawing. A script glues them into one file
at the end. Both versions have their own tests that run right on my Mac without
me installing anything extra.

The best part is that the tests run automatically before the website updates. So
if I break the rules by accident, the broken version never actually goes up.
