title: Supper
kind: Apple app
status: Ready to submit
order: 11
tagline: Plan what you are eating this week, and get one shopping list out of it.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
icon: supper.png
image: supper.png
links: Site | https://z1order.github.io/supper-site/
---

Supper is for the question "what are we eating this week, and what do I need to
buy?" You put meals on days, write down what each one needs, and the app turns
all of that into one shopping list.

It is not a recipe app. A meal here is just a name, how many people it is for,
and the things you have to buy. That is all the planning part actually needs.

## What it does

- **A week at a time**, with breakfast, lunch and dinner on each day. Step
  forward to plan next week, or back to see what you ate last week.
- **One shopping list** built from every meal you planned.
- **Amounts that add up.** 500g here and 250g there becomes 750g. Amounts you
  cannot add, like "1.5kg" and "4", sit side by side instead of getting turned
  into a wrong number. Something you wrote in words, like "a thumb of ginger",
  stays exactly as you wrote it.
- **Sorted the way a shop is**, so you are not walking back and forth.
- **Extra things too.** Milk and bin bags go straight on the list without
  belonging to any meal.
- **Tick things off** as you buy them, and it tells you why each thing is on
  the list.

## The tricky part

Three meals this week want onions. The list should say onions once, not three
times, because you only stop at the onions once.

That sounds easy until you look at what people actually type. One meal says
"Onion", the next says "onions", and the third says "Onions " with a space on
the end. Those are three different words as far as a computer is concerned.

So before comparing two things, the app makes them lowercase, cuts off the extra
spaces, and drops an "s" from the end. Then all three of those turn into the
same thing and become one line. The line keeps whatever spelling you typed
first, so it still looks like something you wrote.

I only merge things inside the same part of the shop, which keeps it safe. The
worst thing that can go wrong is two spellings of the same aisle stop getting
joined, and that was going to happen anyway.

Ticking things off has a small trick in it too. The tick lives on the
ingredient, not on the list. So if you buy paprika for Saturday's dinner, it is
still bought when Sunday's curry asks for it. And if you have bought two of the
three onions, the line tells you that instead of just looking unbought for no
reason you can see.
