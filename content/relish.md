title: Relish
kind: Apple app
status: In development
order: 25
tagline: Ranks every restaurant you've been to by comparing them, not by star ratings.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: relish.png
---

Giving a restaurant a score out of ten sounds easy, but nobody actually
carries a fair ten-point scale around in their head — the number changes with
your mood, and six months later you can't remember if your 8 meant "really
good" or "good, but I was starving." Asking "which of these two was better?"
instead gets a real answer every time, because that's a question people can
actually answer. So in Relish, you never type in a score. You pick a rough
reaction, answer a few "which was better" questions against places you've
already ranked, and your score falls out of where you land.

## What it does

- **Three reactions to start**: loved it, it was fine, not for me. That's
  already most of the sorting done, since a place you loved never has to be
  compared against one you didn't.
- **A handful of head-to-heads** settle the exact spot — a list of a hundred
  places gets sorted in about seven questions.
- **The other place's score stays hidden** during a comparison, so you're
  answering "which did I like more" instead of "do I agree with this
  number."
- **Brings your list over from Beli**, if you already track restaurants
  there, and keeps your existing scores as a starting point instead of
  making you re-rank everything from zero.

## The tricky part

Handing out a perfect 10.0 the first week would be a lie, and it's the kind
of lie that ruins a ranked list — you'd spend the top of the scale
immediately and every place after that would be a letdown by comparison. So
the range a rating can land in gets wider as you rank more places. Your first
loved restaurant might land at an 8.5. Your tenth might land anywhere from
7.4 to 9.7. Nothing hits a true 10.0 until you've actually built a real list
underneath it.

Importing somebody's existing spreadsheet was its own puzzle, because I can't
count on the file being formatted the way I expect. A restaurant name might
have a comma right in the middle of it, like "Katz's Delicatessen, Houston
St," and a naive way of reading the file would split that into two columns by
mistake — working fine for twenty rows and then quietly shifting everything
after that. I had to read the file the careful, correct way instead of the
easy way, and show every guess before saving anything, so a wrong guess is
two taps from fixed instead of a silently ruined import.
