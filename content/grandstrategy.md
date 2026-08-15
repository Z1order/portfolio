title: GrandStrategy
kind: Game
status: In development
order: 2
tagline: A grand strategy game in the spirit of HOI4, with a map you can read.
platforms: Desktop (Godot)
stack: Godot 4.7, C#, .NET 8
icon: grandstrategy.svg
---

A simplified, better-looking grand strategy game. Every launch generates a fresh
world, and the clock starts paused on 1 January 1936.

## What works now

- **A generated world** — a continent, around 420 provinces, eight countries, an
  adjacency graph and per-province industry.
- **A political map** with borders, water shading and a paper-grain texture that
  repaints live as provinces change hands.
- **Cities as the whole economy.** Only a spread-out subset of provinces are
  cities; rural provinces produce nothing, so taking enemy cities is what
  actually wins wars.
- **Armies and combat.** Division stacks pathfind over the adjacency graph;
  moving into an enemy province assaults it, and battles resolve over days with
  a defender advantage.
- **AI opponents** that build armies, declare opportunistic wars and march on
  the front.
- **Victory and defeat.** Conquer the world to win; lose your last province to
  lose.

## Worth knowing

The architecture rule is that the simulation is pure C# and Godot only draws it.
The map generator, the clock, provinces and countries contain no rendering code
at all, which is what lets a 600-day AI-versus-AI balance run happen headlessly
from the command line.

The map trick is that province IDs are baked into a lookup texture as
`id = R + G*256`. Turning a mouse position into a province becomes a single
array lookup, and every question about how the map *looks* — borders, ownership
colours, terrain shading — becomes a shader problem rather than a geometry one.
