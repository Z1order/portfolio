title: Engulf
kind: Apple app
status: Ready to submit
order: 31
tagline: A swarm game for Apple Watch where your army surrounds enemies instead of attacking them.
platforms: Apple Watch (standalone)
stack: SwiftUI, watchOS
icon: engulf.png
links: Site | https://z1order.github.io/engulf-site/
---

Engulf is a game for Apple Watch where you command a swarm of little blobs.
You drag to move them and turn the Digital Crown to spread them out or pull
them in tight. Nothing in your army ever attacks — you win by surrounding an
enemy completely, and the ring of blobs crushes it.

## What it does

- **Drag to move, Crown to resize.** Your army forms a ring around wherever
  you're pointing, and the crown makes that ring wider or tighter.
- **Different enemies need different tactics.** Some die to three blobs
  around them, some need four, and one — the devourer — eats your blobs
  whole until you surround it, at which point it spits every single one back
  out.
- **A boon after every wave**, upgrading your army in one of several ways —
  the best one raises your slain enemies as more blobs for your side.

## The tricky part

Getting the swarm to actually move like one army instead of a mess of
separate dots was harder than I expected. My first idea was to have every
blob aim itself at one leader blob, but that fell apart immediately — the
whole group would stretch into a weird arc and could never actually close a
full circle around anything.

What works instead is having every blob aim for its own spot in the ring, all
spaced out evenly, and figuring out where that spot is using something like
an average direction across the whole group rather than picking one blob to
follow. I also found actual game-breaking bugs by writing a version of the
game that plays itself hundreds of times with no watch involved at all — that
is how I found out a swarm reduced to just one or two blobs could get stuck
forever, unable to finish surrounding anything, which is why the game now
speeds enemies up the longer a wave drags on.
