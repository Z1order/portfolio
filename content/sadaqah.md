title: Sadaqah
kind: Apple app
status: In development
order: 47
tagline: A record of money you give to charity, kept in both the Islamic year and the tax year at once.
platforms: iPhone
stack: SwiftUI, SwiftData, LocalAuthentication
icon: sadaqah.png
---

Most giving leaves no paper trail. A note folded into the box on the way out of
Friday prayer. A transfer to a cousin from the bus. Cash into a tin at a
dinner. If an app asks for a charity name, a category and a photo before it will
save anything, then it saves nothing, and in April you have nothing to look back
at.

So the top of the home screen is an amount and a tap. Everything else can be
filled in later, or never.

## What it does

- **Different kinds of giving stay separate.** Zakat is owed and has a deadline.
  Sadaqah is given freely. Zakat al-fitr is per person and due before the Eid
  prayer. Interest taken off a bank balance is got rid of rather than given, and
  earns nothing. Lump them all together as "donations" and the app cannot answer
  either question you actually have.
- **What you still owe, counting down.** "£1,450 of £2,300 paid, £850 left, due
  in 47 days." Paying it off in pieces across the year is the normal way people
  do it.
- **It never adds up two currencies.** To do that you need an exchange rate, and
  a rate needs a date, and an app that quietly picks one has made up a number you
  might put on a tax return. So each currency gets its own line. If you pay a
  bill in one currency with money in another, you type the rate in yourself and
  it gets saved with that record forever.
- **A missing-receipt list.** In the US, a gift of $250 or more to a registered
  charity needs a letter, and a bank statement will not do. The letter turns up
  in January and by April nobody can find it. The app knows the amount, whether
  the charity counts, and whether you took a photo, so it can just tell you.
- **A PDF for each year**, one for your accountant and one for what you owed.
- **Standing orders that ask instead of assume.** On the day, the app asks
  whether the money actually went out. Cards expire and payments fail, and a
  ledger that invents twelve entries a year and gets one wrong is worse than
  none, because you cannot see the mistake.

There are no streaks, no badges and nothing to share. Giving quietly is the
whole idea, and turning it into a scoreboard would be gross.

## The tricky part

The app has to hold two calendars at the same time, and they do not line up.

The tax year ends on 31 December. The zakat year runs from your own date in the
Islamic calendar, which follows the moon and is about eleven days shorter, so it
walks backwards through the seasons a little every year. That means two gifts on
either side of New Year are in different tax years and the same zakat year. Two
gifts three weeks apart in spring can be the other way round. Neither view is
just a filter on the other, so both had to be built properly.

The part that nearly caught me out is the day the year turns over. A zakat year
ends the moment the next one starts, so a payment made on that exact day belongs
to the new year's window while very often being the payment for the year that
just ended. Those are two different questions. So the app answers them
separately: the dates decide which year a gift shows up in, and you decide which
bill it pays. Mixing those two up is the bug the whole thing is built to avoid.

There is a smaller one hiding underneath. Islamic months are 29 or 30 days long,
and which one it is changes from year to year. So if your date is the 30th of a
month, roughly half the time that day does not exist. Handed straight to the
phone's calendar it silently slides into the next month and drags the whole
year's window along with it. The app pulls it back to the last day the month
really has, and it does that the same way everywhere, so nothing ever falls down
the gap between two answers.
