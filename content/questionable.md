title: Questionable
kind: Game
status: In development
order: 5
tagline: A life simulator where every year of your life is made up on the spot.
platforms: Mac (browser or terminal)
stack: Python, Claude
---

Questionable is a life game, like BitLife. You are born as a random person in a
random town, with random parents. Then you live your whole life one year at a
time, making one choice each year, until you die or reach your life goal. The
twist is that nothing is written ahead of time. Claude makes up every single
year while you play.

## What it does

- **A new person every time.** You get a name, a hometown, a pair of parents,
  one bad habit you will grow into, and one ordinary goal, like owning a boat.
- **One choice per year.** Something happens, and you pick what to do. Sometimes
  the game asks a follow-up first, like what kind of soup, or how hard you pet
  the dog.
- **Your choices stick.** Your answer changes your happiness, health, smarts,
  looks and money. It also goes into a life log, and the game remembers it.
  Something from when you were ten can come back when you are forty.
- **An ending either way.** When you die, you get a gravestone, a short
  obituary and a line from your mother. Every life goes into a hall of fame, or
  a hall of shame.
- **Two ways to play.** There is a page that looks like a phone app in the
  browser, and the same game in a plain terminal window.

## The tricky part

The hard part was getting a computer that writes stories to also keep score.

Every year, the game needs two things back from Claude at the same time. It
needs the funny part, which is what happened. It also needs the numbers, like
"health goes down 10" and "you are now 23". Claude is great at the first part
and a little sloppy at the second. Sometimes it would add a friendly sentence
before the numbers, or wrap them in extra marks, and then my code could not
read any of it. So now, if the answer comes back messy, the game sends it back
once and says what was wrong with it. That fixes it almost every time.

The other hard part was the jokes. My first version was random and silly, with
wizards and ducks and goblins. It got boring fast, because when anything can
happen, nothing is surprising. Now it is only allowed to use real life: a
landlord named Dave, a cousin's business idea, a driving test. That turned out
to be much funnier. I also had to tell it to keep things short, since nobody
wants to read a paragraph before every choice. And a baby should not be asked
about their job, so every year the game reminds Claude exactly how old you are.

To keep lives from all looking the same, each year the game slips in two random
ideas, like a stray dog and a tax bill, and a nudge like "bring back someone
from earlier." Claude has to fit them in somehow.
