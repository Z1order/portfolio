title: Bellwether
kind: Other
status: In development
order: 1
tagline: A robot that trades a fake $100,000 stock account every morning, and shows you how it's doing.
platforms: Mac
stack: Python, Swift, Claude
---

Bellwether is an agent that runs on my Mac every trading morning. It reads
the news, decides what to buy or sell, and places the trades itself — but
the money isn't real. It uses a paper trading account, which is a
practice account that starts at $100,000 and tracks real stock prices
without any actual money moving.

## What it does

- **Researches and trades on its own**, once a day, without me telling it
  what to do.
- **Only ever buys**, never borrows money, and never risks more than a
  small slice of the account on one stock.
- **Double-checks its own decisions** before placing anything, and throws
  out any trade that breaks its own rules instead of shrinking it to fit.
- **Shows up as a card** with what the account is worth, plus a menu bar app
  with the full list of what it holds and why.

## The tricky part

The tricky part was making sure the robot doesn't do anything dumb, since
nobody is standing over it every morning. So the decision-making is split
into two steps: first it writes out its reasoning like a normal paragraph,
and only after that does it turn that reasoning into an actual list of
trades. That way the reasoning stays readable by a person, instead of being
some hidden thing I'd have to guess at.

Then, separately, every single trade it wants to make gets checked against
hard rules before anything happens — nothing over 10% of the account in one
stock, no more than 5 trades a day, and so on. If a trade breaks a rule, it
gets thrown out completely rather than shrunk down to fit. A trade the
robot didn't actually want at a smaller size isn't a trade worth making at
all.
