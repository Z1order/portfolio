title: Marque
kind: Apple app
status: Ready to submit
order: 14
tagline: Helps you pick a car with real numbers, not guessing.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: marque.png
image: marque.png
links: Site | https://z1order.github.io/marque-site/
---

Marque is for the question "which car should I actually buy?" It is not a
listings site and it does not talk to dealers. It just puts the numbers that
actually matter side by side, like what a car will be worth in five years, or
whether paying more for a hybrid ever pays for itself at the miles you
actually drive.

## What it does

- **Every car the government has ever tested for fuel economy** — over 50,000
  of them, going back to 1984 — built right into the app so you can search and
  filter it instantly, even with no internet.
- **About 55 cars people are actually choosing between right now**, each with
  a price, cargo space, warranty details, and my own notes on what is good and
  what to watch for.
- **Filters that match how people actually rule cars out**: budget, body
  style, fuel type, and things like how many seats or how much towing you
  need.
- **Compare up to four cars side by side**, about twenty rows of numbers, with
  the best one in each row highlighted.
- **A five-year cost estimate** that adds up losing value, gas or charging,
  insurance, repairs, and loan interest — with every number editable, so you
  can put in your own guesses instead of mine.
- **Live crash-test ratings**, pulled right from the government's own site.

## The tricky part

Nobody publishes the real cost of owning a car. You have to estimate it, and
the biggest piece of that estimate, usually bigger than gas and insurance put
together, is how much value the car loses every year. That number is the one
buyers never see until they go to sell.

I built a curve for that instead of one flat number, since a new car loses
value fast in year one and then slows down. The app models three speeds of
that curve, slow, average, and fast, and picks one based on the car. For cars
I have not personally researched and written notes on, the app only shows the
free government numbers, like fuel economy, and says plainly that it has no
price or resale guess for that one. I would rather the app admit it does not
know than make up a number that looks official but is not.
