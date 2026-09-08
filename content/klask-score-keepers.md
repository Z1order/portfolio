title: Klask Score Keepers
kind: Other
status: Live
order: 5
tagline: Replacement score discs for a board game, built out of maths instead of a drawing program.
platforms: 3D printer (STL file)
stack: Python
---

Klask is a board game, and it comes with two little discs you slide along the
side of the board to keep score. This makes a new pair of them. It is one short
Python program, and running it writes a file a 3D printer can open.

## What it does

- **Makes the disc out of numbers.** Thirty millimetres across and three
  millimetres thick, which is about the size of a coin. I never opened a
  drawing program. The shape is a circle worked out with sine and cosine,
  chopped into a hundred and eighty little steps around the edge.
- **Slopes the top edge in slightly** so the finished disc does not have a sharp
  lip you can feel with your thumb.
- **Puts both discs on the plate at once**, side by side, so one print gets you
  the pair.

## The tricky part

A 3D printer does not really understand a disc. All it gets is a pile of
triangles, thousands of them, stuck together to make a skin. If that skin has a
gap anywhere, even one you would never see, the printer has no way of telling
what is inside the shape and what is outside it, and the print comes out wrong
or the software just refuses.

So the program checks its own work before I ever open the file. Think of the
skin as a patchwork quilt. Every edge in it has to be sewn to exactly one other
patch — not zero, and not two. The program goes through every edge, counts how
many times it turns up, and tells me how many are unmatched. It should always be
none.

The other thing it checks is which way the triangles face. Every triangle has a
front and a back, and they all have to face outwards. If they are inside out the
printer thinks the whole world is the object and the disc is the empty part.
There is a nice trick for that: if you add up the space inside the shape and the
answer comes out negative, you built it inside out. So the program adds up the
space and prints the number, and I look at it before I print. That check cost me
about five lines and it has saved me from wasting plastic.
