title: RayArena
kind: Game
status: In development
order: 4
tagline: A first-person team shooter I wrote from nothing in Python, with maps you can climb.
platforms: Mac (Python and pygame)
stack: Python, pygame
---

RayArena is a first-person shooter. You are on the blue team with three
computer teammates, against four computer players on red, and the first team to
twenty kills wins. There is no game engine underneath it. The whole picture is
drawn by hand, one thin vertical strip at a time.

## What it does

- **Five maps**, each one written as rows of letters in the code. A `#` is a
  wall, a `1` is a platform you can stand on, an `s` is a step up onto it. So
  building a new map is really just typing a picture of it.
- **Three guns.** A rifle, a shotgun that fires six pellets at once, and a
  sniper you can scope in with, which drops your view down to a narrow slice and
  makes the shot almost perfectly straight.
- **Bots that use the map.** They find their way to you around corners instead
  of walking into walls, they wait a moment before they start shooting so they
  are not inhuman, and they spread out instead of bunching into a clump.
- **Mouse look, sprinting and fullscreen**, with the sensitivity saved between
  games so you only set it once.

## The tricky part

A game like this draws the world in vertical strips, like a bar code. For each
strip it fires one invisible line straight out from your eye, sees the first
wall it hits, and paints a slice of that wall down the strip. Do that two
hundred and forty times across the screen and you get a room. My first version
worked exactly like that, and every floor in it was flat.

Adding upstairs broke the whole idea. Once the ground can be at different
heights, one strip is not one thing anymore. Looking across a room you might see
the top of a low step, then a taller platform behind it, then a wall behind
that, with sky in the gaps. The line cannot stop at the first thing it touches,
because there is more of the picture above it.

What I do now is keep going. The line walks outward through the map, and every
time the ground changes height it paints that surface. The trick is that each
strip remembers the lowest row of pixels it has already coloured in. Anything
further away is only allowed to paint above that line, never below it. That one
rule is what stops a far wall from painting over the platform in front of it,
and it also does the sorting for free, because near things get painted before
far things get a chance.

Players had to follow the same rule. I keep the whole list of "how far away, and
how low had I painted by then" for every strip, so when I draw a teammate I can
check that list and hide the part of them that is behind a wall. That is why
somebody standing on a roof shows up properly instead of appearing to float in
front of it.
