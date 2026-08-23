title: Double Sir
kind: Apple app
status: In development
order: 49
tagline: The card game my family plays, with a computer opponent, a pass-and-play mode, and a scorekeeper for real cards.
platforms: iPhone
stack: SwiftUI
icon: double-sir.png
---

Court Piece is a four-player card game with partners sitting opposite each
other. My family plays it with an extra rule called the double sir, and no app
I could find plays it that way.

The normal game gives a trick to whoever wins it. With the double sir, tricks
you win pile up in the middle of the table instead, and you only get to keep
them by winning two in a row. So one good round is worth nothing on its own, and
two in a row can be worth six.

There are three ways to use the app: play against the computer, pass one phone
around four people, or just keep score for a game with real cards.

## What it does

- **Three opponents that actually play.** You sit at the bottom and the app
  plays your partner and both opponents. There are three difficulty settings,
  and the hardest one remembers which players have run out of which suits.
- **Pass and play** for four people and one phone, with your hand covered up
  between turns.
- **A scorekeeper for real cards.** Tap who won each round and the app keeps
  track of the pile in the middle, who is on a streak, and the score. This is
  the mode I use most, because the pile is the part everyone argues about.
- **The whole rule set**, including the odd endings: whoever is winning stops at
  seven, an even split is a dead hand and gets dealt again, and anything left in
  the middle at the end just disappears.

## The tricky part

The rule about the pile in the middle turned out to be the only thing in the
whole app worth writing carefully, so I wrote it once and everything else uses
it.

The playable game and the scorekeeper are completely different screens, but they
both need the same answer to the same question: given the list of who won each
round, in order, what is in the middle right now and who has what? If I had
written that twice, the two would drift apart, and the version people trust
least is the one that disagrees with the cards on the table.

So the app does not really store a score at all. It stores the list of who won
each round, and works the rest out from that list every time. That made undo
free. Tapping the wrong person is the single most common thing that happens with
a scorekeeper, and undoing it is just dropping the last item off the list and
running through it again. There is no separate untangling step that could get
the answer slightly wrong.

The other thing I had to rethink was the computer players. My first version
tried to win every round, which is what you would do in almost any other card
game, and it played terribly. In this game a round is worth almost nothing by
itself. It is worth a lot when it takes the whole pile, and it is worth just as
much when it stops the other side taking the pile. So the computer stopped
asking "can I win this round" and started asking "what is on the table right
now, and who is one win away from taking it".
