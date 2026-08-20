title: Morsel
kind: Apple app
status: Ready to submit
order: 35
tagline: A photo diary of what you ate, so a year from now it can hand the day back to you.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: morsel.png
image: morsel.png
links: Site | https://z1order.github.io/morsel-site/
---

You take a picture of your food. That's it, that's the whole app. No typing
what you ate, no counting calories. A year later the app shows you that same
day, and you get to see a lunch you completely forgot about, in a place you
haven't been back to in a while.

## What it does

- **One photo, one entry.** The app guesses whether it's breakfast, lunch,
  dinner, or a snack from the time of day, so you don't have to pick.
- **A year-ago card**, right on your main journal screen, not buried in some
  tab you'd never open. If you logged something around this day last year, it
  shows up automatically.
- **A places list** that groups your photos by where you ate, even if you
  typed the name a little differently each time.

## The tricky part

The whole point of the app is showing you "this day, a year ago." But most
people don't eat out at the exact same time every day, so a lot of days would
come up completely empty. An empty feature on day one is how an app gets
deleted before it even gets good.

So instead of only matching the exact date, the app looks three days on
either side too. "Around this time last year" is still true, and it turns an
empty screen into an actual memory way more often. I also had to make sure
the app doesn't save your photos at full size — a year of three meals a day
at full camera quality would eat a huge amount of space on your phone for
no reason, so every photo gets shrunk down to about a fortieth of the size
before it's stored.
