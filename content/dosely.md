title: Dosely
kind: Apple app
status: Ready to submit
order: 8
tagline: Reminds you to take your medicine, and keeps reminding you until you do.
platforms: iPhone (iOS 17+)
stack: SwiftUI, SwiftData, WidgetKit
icon: dosely.png
image: dosely.png
---

You tell Dosely what medicine you take and when, and it reminds you at that
time. If you do not mark it as taken, it reminds you again. It handles the easy
kind of medicine, like a pill every morning, and the harder kind, like a shot
every two weeks.

## What it does

- **Every two weeks, not just every day.** A shot on a two week schedule is
  something most medicine apps cannot even describe. Dosely works out the actual
  dates and sets a reminder for each one.
- **It keeps nudging.** After the first reminder, it can send up to six more,
  as far apart as you want. They stop the second you say you took it.
- **A widget with a countdown.** Your next dose sits on your home screen or lock
  screen with a timer, and a Taken button so you never have to open the app.
- **It cuts through Do Not Disturb**, because a dose is the kind of thing that
  should get through.

## The tricky part

Two things fought each other here.

The first one is that a single reminder is really easy to miss. If your phone
buzzes at 9:00 while your hands are wet, by 9:05 the notification is gone and so
is the thought. That is why every medicine can have a whole string of follow-up
reminders instead of just one.

But the iPhone will only hold 64 reminders at a time, and it does not warn you
when you go over. It just quietly throws the extra ones away. One medicine
taken twice a day with six nudges each is already twelve reminders per day, so
you run out of room in under a week. Everything after that silently disappears.

So Dosely does not try to schedule everything. It builds every reminder for the
next month and a half, puts them in order, and only hands the phone the
earliest sixty. Then every time you open the app it throws them all out and
builds them again, which quietly slides that window forward. You never notice
it happening, and you never hit the limit.

I also had to be careful with the Taken button on the widget. It only shows up
when the dose is within half an hour of being due. Otherwise you tap it by
accident on something that is not due until tonight, and now your log says you
took a dose you did not take. A medicine log you cannot trust is worse than no
log at all.
