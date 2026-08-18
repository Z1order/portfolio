title: Cadence
kind: Apple app
status: In development
order: 17
tagline: A habit tracker that tells you what you meant to do, not just what you already did.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: cadence.png
---

Cadence is for habits you want to keep. You say what you want to do and how
often, and the app reminds you on the days it is actually due.

It is the other half of [Streak](../streak/), another app I made. Streak is a
log of things you already did. Cadence is for things you plan to do, before
you have done them.

## What it does

- **Four ways to say how often**: every day, certain days of the week, a
  number of times a week on whatever days you like, or every few days.
- **Today shows what is left and what is done**, both at once, so a list that
  empties itself as you check things off does not erase the credit for what
  you already did this morning.
- **A week strip across the top** rings each day with how much of it you
  kept, and yesterday is one tap away if you forgot to check it off before
  bed.
- **Reminders that leave you alone** once you have already done the thing —
  no nagging at 9pm for something you did at 7am.
- **A number on the app icon** that matches exactly how many things are left
  today.
- **A history grid** that can tell a day you missed apart from a day the
  habit never even asked about.
- **Archiving.** Stopping a habit does not erase the months you kept it.

## The tricky part

The easy way to set a daily reminder is to tell the phone "remind me every
day at 6pm" and let it repeat forever. The problem is once you have already
done the habit that day, there is no way to cancel just that one repeat and
leave the rest running. The reminder goes off anyway, telling you to do
something you already did.

So instead, the app schedules one reminder at a time for each day, for about
the next three weeks, and rebuilds that whole list every time you open the
app or check something off. If you already did today's habit, today's
reminder for it just is not on the list anymore.

There is a limit hiding in this too: the phone will only hold 64 reminders at
once for the whole app, no matter how many habits you are tracking. So every
candidate reminder gets sorted by which one is coming up soonest, and only
the soonest 60 get kept. As long as you check in every few weeks, the list
stays full and you never notice the limit is even there.
