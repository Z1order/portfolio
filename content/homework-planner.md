title: Homework Planner
kind: Apple app
status: Live
order: 1
tagline: Homework tracking that follows you from desk to wrist.
platforms: iPhone, iPad, Mac, Apple Watch (iOS 17+)
stack: SwiftUI, SwiftData, CloudKit
icon: homework-planner.png
image: homework-planner.png
links: App Store | https://apps.apple.com/us/app/homework-planner-for-students/id6797358318 ; Site | https://z1order.github.io/homework-planner-site/
---

Add an assignment with a title, class, description, due date and an optional
photo of the board. Mark it done and it moves into an archive rather than
vanishing. Everything syncs through your own iCloud, so there is no account to
make beyond the Apple ID you already have.

## What it does

- **To Do.** Every pending task, soonest due date first, overdue ones in red.
- **Add a task** with a photo taken on the spot or picked from your library.
- **Archive.** Finished work, swipe to restore or delete for good.
- **On the watch.** Pending homework, tick something off, add an assignment.

## Worth knowing

Every device keeps its own store and syncs through the private iCloud database
rather than mirroring a designated main device. That sounds like a detail until
you are on a bus without your phone: the watch is still current, because it
talks to iCloud directly rather than to the iPhone in your bag.

The same code has to run where iCloud is unavailable — in the Simulator, or
before a development team is selected — so the container falls back to a
local-only store instead of failing to launch. Two devices that seem not to be
syncing are usually two devices that both took that fallback.
