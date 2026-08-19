title: Streak
kind: Apple app
status: Live
order: 3
tagline: A list of stuff you already did, not stuff you are supposed to do.
platforms: iPhone (iOS 18+), home screen widget
stack: SwiftUI, SwiftData, WidgetKit
icon: streak.png
image: streak.png
links: App Store | https://apps.apple.com/us/app/streak-activity-log/id6799180435; Site | https://z1order.github.io/streak-site/
---

You played tennis, so you open the app and tap Tennis. If Tennis is not on your
list yet, there is a New button sitting right next to everything else that adds
it for good. Your streaks and stats come from what you actually did. The app
never asks you to plan anything, and it never tells you that you should have
done more.

## What it does

- **One tap** for the thing you just finished. You can add how many minutes it
  took if you want.
- **Streaks and stats** built from your list, not from a schedule you set up.
- **A widget** on your home screen so you can see your streak without opening
  anything.

## Why I built it this way

The app and the widget both use the exact same save file instead of copying
things back and forth. The widget literally opens the file the app writes to.
That is why the app has to poke the widget after every save — the widget can
read the file, but it does not notice on its own when the file changes.

The rule I had to think about hardest: your streak does not break just because
you have not done anything *yet today*. It is 9 in the morning. Of course you
have not gone running. If the app showed your 40-day streak as a zero every
single morning, you would get annoyed and delete it. So the streak counts from
today if you already logged today, and from yesterday if you have not.
