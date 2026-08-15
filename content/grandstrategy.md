title: GrandStrategy
kind: Game
status: In development
order: 2
tagline: A war strategy game like HOI4, but with a map you can actually read.
platforms: Desktop (Godot)
stack: Godot 4.7, C#, .NET 8
icon: grandstrategy.svg
---

A strategy game where you run a country and try to take over the world. It is
based on Hearts of Iron 4, but simpler and better looking. Every time you start
it, you get a brand new map you have never seen before. The clock starts paused
on January 1st, 1936.

## What works so far

- **A map that builds itself** — one continent, around 420 different regions,
  eight countries, and factories spread around.
- **A map you can read**, with country borders, shaded water, and a paper
  texture. It repaints itself as you take land, so you can watch your color
  spread.
- **Cities are everything.** Only some regions are cities, and only cities make
  anything. Empty countryside gives you nothing. That means taking your enemy's
  cities is how you actually win instead of just grabbing land.
- **Armies and battles.** You click your army and right click where you want it
  to go. Moving into enemy land starts a battle, and battles take a few days,
  with the defender having the advantage.
- **Computer countries** that build armies, declare war when they think they can
  win, and march to the front.
- **Winning and losing.** Take the whole world to win. Lose your last region and
  you are out.

## Why I built it this way

I made one rule for myself: the game logic is not allowed to know anything about
drawing. The map builder, the clock, the regions, and the countries have zero
drawing code in them. That rule is annoying at first, but it is why I can run
600 days of computers fighting each other with no window open at all, just to
see if the game is balanced.

The map has one trick I am proud of. Every region gets a secret ID number hidden
inside a special image, stored as a color. So when you move your mouse, the game
does not have to check 420 shapes to see which one you are pointing at. It just
looks up the color under your cursor. That one idea also turns every map
question — borders, who owns what, terrain colors — into a coloring problem
instead of a shape problem, which is much faster.
