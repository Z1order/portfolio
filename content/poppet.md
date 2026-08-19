title: Poppet
kind: Apple app
status: In development
order: 20
tagline: Works out the safe dose of kids' medicine by weight, at 3am, in seconds.
platforms: iPhone
stack: SwiftUI, SwiftData, WidgetKit
icon: poppet.png
image: poppet.png
---

Kids' medicine is dosed by weight, but the bottle in the cupboard is labeled
by age, and those two things don't always agree. Poppet stores each of your
kids' weight once, and after that the answer is one screen: this kid, this
medicine, this many milliliters, and when the next dose is allowed. I built
it for the exact moment nobody wants to do math — the middle of the night,
with a crying kid in the room.

## What it does

- **Works out the dose from weight first**, using real published medical
  guidelines, then never lets that number go above what the bottle's age
  range allows. Weight can only ever make the dose smaller than the label
  says, never bigger.
- **Rounds down, always**, to the smallest amount the syringe can actually
  measure. Every rounding mistake in this app points toward the safer number.
- **Tells you exactly when the next dose is allowed**, checking three rules
  at once — hours since the last dose, doses in the last day, and total
  milligrams in the last day — and gives you whichever one is strictest.
- **A widget** showing both medicines at a glance, and whether it's safe to
  give one right now.
- **Refuses to answer** when it shouldn't. Too young, too light, or a dose
  too small to measure, and it tells you to call a doctor instead of
  guessing.

## The tricky part

The scariest kind of bug in an app like this is one where the display and the
real answer quietly disagree — like a widget saying "OK now" a few minutes
before it actually is. So I made sure every number anywhere in the app,
including the widget, is calculated the exact same way, off the same list of
doses actually given. Nothing is stored as a separate "current answer" that
could get out of sync with the real history.

I also had to think hard about what the app should refuse to do. It would be
easy to make a calculator that always spits out a number. But a number is not
always safe — under three months old, or a dose too small to measure — and in
those cases the right answer is "I don't know, go ask someone," not a
confident-looking milliliter figure that happens to be wrong.
