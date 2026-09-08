title: World Economy
kind: Game
status: In development
order: 3
tagline: Run one real country, one year at a time, and try to be the last one standing.
platforms: Mac (terminal or window)
stack: Python, pygame, rich
---

World Economy is a game where you are put in charge of one real country. Every
turn is one year. Fifteen other countries are run by the computer, and the game
does not end until all of them have fallen apart, or you have.

## What it does

- **Five things to run every year.** Taxes and spending, the central bank,
  trade and tariffs, laws and policing, and which kind of science your country
  pays for.
- **One world market.** Whatever your country makes and does not use gets sold.
  Whatever it needs and cannot make gets bought. Everybody trades in the same
  place, so a bad harvest in one country shows up as a higher food price in all
  of them.
- **Countries actually collapse.** Borrow too much and you stop being able to
  pay, which wrecks your money and locks you out of borrowing for five years. Do
  it three times and you are finished.
- **Years that go wrong on their own.** Oil shocks, droughts, pandemics, bank
  failures, strikes and scandals turn up on their own, and most of them ask you
  to pick what to do about it.
- **Two ways to play.** A window with a world map, charts and tabs, or the same
  game in the terminal. A tutorial walks you through the panels the first time
  and then stays out of your way.

## The tricky part

The hardest part was food, and it was not the growing of it. It was deciding
who goes without.

Some years the world does not grow enough food for everyone. Somebody has to
miss out. My first version split the shortage evenly, so every country got the
same share of what it needed, maybe ninety percent each. That sounds fair, but
it made the game wrong. Nothing bad ever happened to anybody in particular. Real
shortages are not like that. When food runs short, the countries with money and
strong currency buy it first, and the poorest countries are the ones that go
hungry.

So now the game hands the food out in rounds. Richer countries with stronger
money get served first, and what is left over goes to everyone else. A country
that misses too much food three years in a row collapses. The first time I ran
it that way, half the world starved at once, which told me the farming numbers
I had picked were far too low.

Prices took me even longer. At first every price floated on its own, and one bad
turn could push all of them down together, again and again, until everything in
the world was nearly free. I fixed it by making prices relative. The world's
whole shopping basket always costs exactly one, so a price can only go up if
some other price goes down. Cheap food now means food is cheap compared to cars,
which is what I meant by a price the whole time.
