title: Podium
kind: Apple app
status: Ready to submit
order: 26
tagline: Ranks the movies, shows, books and music you've watched, heard and read.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: podium.png
image: podium.png
links: Site | https://z1order.github.io/podium-site/
---

Nobody actually has a fair ten-point scale in their head. Ask someone to
score a movie out of ten and they'll be inconsistent within a week. Ask
"which of these two was better?" instead, and they'll answer instantly and
mean it. So Podium never asks for a number. You give a quick gut reaction —
loved it, it was fine, not for me — and then answer a few head-to-heads
against things you've already ranked. Your score comes out of where you land.

## What it does

- **A few quick comparisons** settle your exact spot on the list — around
  seven questions sorts a list of a hundred things.
- **Rankings stay separate by type.** Songs only ever get compared to songs,
  movies only to movies, because "was this three-minute song better than
  this whole novel" isn't a real question.
- **An Everything view** that still works, because even though rankings are
  separate, the scoring bands mean an 8.4 book and an 8.4 movie both mean
  "near the top of what I loved" — so they can sit on one combined list
  honestly.
- **A backlog**, grouped by type, so *songs to hear* and *books to read* stay
  in their own lanes too.

## The tricky part

The scale had to actually mean something, so I split it into three bands —
one for "loved it," one for "it was fine," one for "not for me" — and those
bands never overlap. That's the rule that makes the whole thing trustworthy:
something you loved can never accidentally score lower than something you
didn't, no matter how the comparisons inside each band shake out.

I also had to be careful not to hand out a perfect score too easily. A 10.0
after only two ranked movies would be meaningless, so the range each band can
use starts narrow and only widens as you rank more things in it. It takes a
real list before anything can actually reach the top of the scale.
