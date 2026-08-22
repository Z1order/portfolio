title: Batch
kind: Apple app
status: In development
order: 42
tagline: Scales a recipe up or down for a different number of people, the right way.
platforms: iPhone
stack: SwiftUI, SwiftData
---

Batch is for when a recipe is written for four people and you are cooking for
eleven. You paste in the ingredient list, tell it how many you are cooking for,
and it scales every line for you. Paste a recipe once and read the answer, no
account and no saving required, though you can save the ones you make a lot.

## What it does

- **Scales more than just multiplying.** Every ingredient gets scaled the way
  it actually should, not just times three.
- **A library** for recipes you cook over and over, so the app remembers how
  you fixed each ingredient last time.
- **Warnings at the top of the screen**, where you'll actually see them before
  you start cooking, not at the bottom.
- **Rounds to real measurements.** No more "3.7 teaspoons" — it rounds to
  something you can actually measure, like an eighth of a teaspoon.
- **Works in any language**, since it just looks for the ingredient word, in
  any script.
- **Share as text or a PDF**, for whoever's actually standing at the stove.

## The tricky part

Tripling a recipe by multiplying every number by three sounds right and is
completely wrong. Triple the salt and chilli in a recipe and it comes out way
too spicy, because how hot something tastes does not go up in a straight line
with how much you add. The water in a dal is the same problem in reverse — a
bigger pot loses less water to steam for its size, so it needs less water
added per person, not more.

So every ingredient in the app belongs to a class, and each class has its own
rule for how fast it grows. Bulk food like rice and dal scales straight up.
Spice and heat grow slower than the rest of the recipe. Water and oil in a pan
grow slower too. A few things, like "a pinch of salt" or "garnish to taste,"
do not scale at all, because the person who wrote the recipe already decided
that number and the app should not touch it.

The other tricky part is figuring out which word is which ingredient, since
the same ingredient gets called different things by different people. The app
picks the longest matching word it finds, so "chilli powder" gets treated
differently than plain "chilli," and "unsalted butter" is recognized as
butter and not as salt.
