title: Qada
kind: Apple app
status: In development
order: 37
tagline: A ledger for the prayers and fasts you're making up, so you always know how many you have left.
platforms: iPhone, home screen widget
stack: SwiftUI, SwiftData, WidgetKit
icon: qada.png
image: qada.png
links: Site | https://z1order.github.io/qada-site/
---

If you're making up missed prayers or fasts, keeping count in your head or on
a random note gets hard fast, and once you lose count it's easy to lose the
habit too. Qada is a simple ledger: it tells you how many you still owe and
whether you're actually catching up, and you can log one with a single tap.

## What it does

- **A remainder and a pace**, right on the main screen, like "about 15 a week
  lately, at that pace you're done by April 2030." A number by itself feels
  like a wall. A number with a date attached feels like something you can
  finish.
- **An estimator** for your starting count, so you don't have to do the math
  yourself. You give it a stretch of time, and it figures out how many
  Ramadans or how many days of prayers fall inside it.
- **A widget** that just shows your remainders, nothing else, no notifications
  guilt-tripping you about a number.

## The tricky part

The app has to let you correct your count without ever making it look like
you lost progress. Say you've logged 126 makeups already, and then you
recount and realize you actually started with 200 more than you thought. The
app has to add those 200 on top without touching the 126 you already did, and
without your weekly pace suddenly looking like it dropped.

I fixed this by keeping two totally separate things: the total you've ever
owed, and the makeups you've actually logged. A correction only changes the
first number, never the second, so your pace line never even flickers when
you fix your count. I also had a bug in an early version where a chart I was
using would quietly merge two bars that had the same label, even though they
were a year apart, and it would just add their numbers together without
telling me. That one took a while to notice because the chart still looked
completely normal, just wrong.
