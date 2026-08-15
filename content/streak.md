title: Streak
kind: Apple app
status: In App Store review
order: 3
tagline: A log of what you actually did, not a list of what you meant to do.
platforms: iPhone (iOS 18+), home screen widget
stack: SwiftUI, SwiftData, WidgetKit
image: streak.png
links: Site | https://z1order.github.io/streak-site/
---

You played tennis, so you open the app and tap Tennis. If Tennis is not in your
list yet, the New chip sitting right next to the others puts it there for good.
Streaks and stats are derived from that record. The app never asks you to plan
ahead, and it has no opinion about what you should have done.

## What it does

- **Tap to log.** One tap for the thing you just did, optional minutes after.
- **Streaks and stats** computed from the log, not from a schedule.
- **A widget** on the home screen showing where you stand.

## Worth knowing

The app and the widget share a single database in an App Group container rather
than syncing between two copies. The widget opens the same file the app writes
to, which is why the app nudges the widget to reload after every save — the
widget reads the store but does not watch it.

The one rule worth arguing about: a streak survives an unlogged *today*. At 9am
you have not done anything yet, and an app that shows your 40-day streak as zero
every single morning is telling you something you will resent. The count starts
at today when today is logged, and at yesterday otherwise.
