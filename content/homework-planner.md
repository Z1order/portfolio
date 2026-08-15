title: Homework Planner
kind: Apple app
status: Live
order: 1
tagline: Keeps track of your homework on your phone and your watch.
platforms: iPhone, iPad, Mac, Apple Watch (iOS 17+)
stack: SwiftUI, SwiftData, CloudKit
icon: homework-planner.png
image: homework-planner.png
links: App Store | https://apps.apple.com/us/app/homework-planner-for-students/id6797358318 ; Site | https://z1order.github.io/homework-planner-site/
---

You type in an assignment with a title, the class it is for, when it is due, and
a photo of the board if you took one. When you finish it, you tap it done and it
moves to a finished list instead of just disappearing. Everything saves to your
own iCloud, so you do not have to make an account.

## What it does

- **To Do.** All your homework, with the stuff due soonest at the top. Late work
  shows up in red.
- **Adding homework.** Take a photo of the board right there, or pick one you
  already have.
- **Finished.** Everything you have turned in. Swipe to put it back or delete it.
- **On your watch.** See what is due and check things off without getting your
  phone out.

## Why I built it this way

Each device saves its own copy and talks to iCloud on its own. That sounds like a
boring detail, but it is the reason the watch still knows your homework when your
phone is in your backpack across the room. If the watch had to ask the phone,
you would be stuck.

The app also has to work when there is no iCloud at all, like when I am testing
it on my computer. So if it cannot reach iCloud, it just saves everything on the
device instead of refusing to open. If two devices are not showing the same
homework, that is usually why.
