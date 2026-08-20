title: Daybook
kind: Apple app
status: Ready to submit
order: 19
tagline: A diary app with one page per day, and nothing else to decide.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: daybook.png
links: Site | https://z1order.github.io/daybook-site/
---

Most journal apps are really just note apps with a date stuck on them. You can
write six entries on Tuesday and none on Wednesday, and the app has no idea
that's weird. Daybook works differently: a day gets one page, and that one
rule is what makes everything else about the app make sense. The calendar can
color in a day. A streak actually means something. Opening the app puts you
on today, with today's page ready to go.

## What it does

- **Today, first.** The app opens on today's page every time.
- **A page per day**, with a mood if you want one. A day you write with no
  mood stays exactly that — the app never quietly counts it as "fine."
- **A calendar** with every day colored by how it felt, plus what you wrote on
  this day in past years.
- **Streaks and stats** — your current streak, your longest one, and a chart
  of how consistent you've been.
- **Search** across everything you've ever written.
- **A lock**, with Face ID or your passcode, so the diary is actually private.
- **Plain text export.** A ten-year diary should not depend on this app still
  existing in ten years, so you can always get every word back out in a
  format anything can open.

A streak you haven't written today doesn't break at midnight — it only breaks
once the day is actually over. Nobody wants an app nagging them at 11:58pm
because they hadn't written yet that morning.

## The tricky part

I keep everything completely on the device — no account, no server, nothing
sent anywhere. SwiftData, the tool I use to store the entries, actually turns
on iCloud syncing by itself the second you add certain permissions to the
app, so I had to go out of my way to turn that back off. A private diary
should stay private by default, not by accident.
