title: Sides
kind: Apple app
status: In development
order: 48
tagline: Splits whoever turned up tonight into even teams, using the results of every game the group has played.
platforms: iPhone
stack: SwiftUI, SwiftData
---

Picking teams with two captains takes five minutes, gets done badly, and stings
whoever gets called last. Picking at random is worse — you get a 9–2, everyone
goes home early, and the evening is gone.

Sides does it in about four seconds. You tap who showed up, tap Split, and it
uses the results of every game the group has already played to make the two
sides even. Nobody has to judge anybody out loud, which is the actual problem
with picking teams.

## What it does

- **It never shows you how good anyone is.** Not a number, not a rank, not a
  list. There is no screen in the app where you can find it out.
- **It tells you about the teams instead.** "Teams are within 2%. An even game."
  That is about the teams, not about a person. You cannot work backwards from it
  to what anybody is worth, and there is nothing in it to screenshot into the
  group chat.
- **Move someone if you disagree.** Drag a player across and the app tells you
  what it cost: "That cost 17% of balance." Then it gets out of the way. It
  suggests, you decide.
- **Rules it will not break.** A dad and his son on the same side. Two people who
  argue every week kept apart. One goalkeeper per team. If what you have asked
  for is impossible, it says which rule and why, in a sentence you can do
  something about.
- **It mixes people up.** When two splits are about equally fair, it picks the
  one that breaks up whoever has played together most recently. Being with the
  same four people every week is its own kind of boring.
- **The only number about a person anywhere in the app** is how many games they
  have played. How often you turn up is your business. How good you are is
  nobody's.

## The tricky part

Keeping the ratings hidden is not me being lazy about a screen. A Sunday
football group where everyone can see that Faisal is rated higher than they are
is a group that stops being fun, and the app would get the blame, fairly. The
ratings exist for one thing — picking the teams — and that thing does not talk.

The harder problem was actually finding the fairest split. With 24 people and
two teams there are about 2.7 million ways to divide them up, and I wanted the
best one, not a decent one. Written the plain way, adding up everyone's rating
for every possible split is around thirty million bits of adding, and the button
stops feeling instant.

So instead of adding people up one at a time, the app adds them up eight at a
time, using a table it works out once at the start. Three lookups instead of
walking through twelve people. That takes the whole thing down to about a
quarter of a second, and it still checks every single split.

Above 24 people it stops being possible to check them all, so it makes a
sensible guess and then keeps swapping people until swapping stops helping,
starting over from 32 different beginnings. When it does that, it says so. It
never pretends a good guess was the perfect answer.

The last thing I learned the hard way: nobody's rating is stored anywhere. The
app keeps the list of games and works every rating out again from scratch every
time. That sounds wasteful, and it is a few hundred sums, which is nothing. But
it means deleting a game you typed in against the wrong team actually undoes it,
and puts every rating back to exactly what it was before. Not nearly — exactly.
Trying to unpick one game from a running total is not really possible, because
how much a game moved someone depends on how many games they had played, which
depends on the games you are trying to remove.
