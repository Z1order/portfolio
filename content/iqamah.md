title: Iqamah
kind: Apple app
status: In development
order: 45
tagline: Tells you when to leave home so you actually get to the masjid before the prayer starts.
platforms: iPhone, Apple Watch, home screen widget
stack: SwiftUI, SwiftData, WidgetKit, WatchConnectivity
icon: iqamah.png
---

Every prayer app works out prayer times from the sun. But the time that
actually matters is the one your masjid picked and taped to the door. My masjid
prays Fajr at 6:00 all winter, no matter what any app says. Iqamah keeps both
times and never mixes them up.

The one thing the app is really for is a single alert: **leave now if you want
to make it.** That is your masjid's time, minus how long the drive takes, minus
a few minutes for wudu and parking.

## What it does

- **Two kinds of time, kept apart.** The one from the sun is printed small and
  grey. The one your masjid announced is printed big and dark, and everything
  else counts backwards from it.
- **Settings for each prayer, not one big switch.** Most people go to the
  masjid for some prayers and pray the rest at home or at work. So each prayer
  has its own masjid and its own alerts. Friday prayer gets its own row again,
  because a lot of masjids run two of them.
- **A photo of the printed timetable.** The sheet on the door is the real
  thing. If a time looks wrong in six months, the photo is the only way to tell
  whether the masjid changed it or I typed it in wrong.
- **It stops nagging you when you are far away.** If you are three hundred
  miles from your masjid, "leave now" is silly. The app pauses those alerts,
  and it says on screen that it did, so you never think it broke.
- **A widget and a watch face**, because this is an app you look at far more
  often than you open.

## The tricky part

iPhones only hold 64 alerts for one app at a time. Ask for more and the phone
throws the extra ones away without telling you.

Five prayers, up to four alerts each, seven days ahead — that is 140. The phone
keeps 64 and quietly bins the rest. Nothing goes wrong that you can see. Your
alerts just stop somewhere around Wednesday, and you find out by missing a
prayer.

So the app never tries to book a whole week. It builds every alert the next
three days would want, sorts them by when they go off, and keeps the 56 that
happen soonest. Fifty-six, not sixty-four, so there is room left over and the
phone is never the one deciding what to drop. Then it throws the whole list
away and builds it again every time you open the app.

Spending your alerts on what happens soonest is the only way that still works
if you do not open the app for a day. Any other way lets Thursday's afternoon
prayer push out tonight's.

Because the app can only promise so far ahead, Settings just tells you the
truth: "Queued alerts, 23 of 64" and the date it has planned through. If that
date ever stops moving forward, something is broken, and you can see it instead
of guessing.

The other thing I got wrong at first was up north. Above about 48 degrees there
are nights in summer when the sun never goes far enough below the horizon for
Fajr to happen at all. My first version made a number up. So now every time the
app works out can come back as nothing, and the screen says so, all the way
from the maths to the widget.
