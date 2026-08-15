title: HW Schedule
kind: Apple app
status: Ready to submit
order: 6
tagline: Tells you what class you have next without making you count days.
platforms: iPhone, Apple Watch
stack: SwiftUI, Vision
icon: hw-schedule.png
image: hw-schedule.png
links: Site | https://z1order.github.io/hwschedule-site/
---

My school runs on an eight-day schedule with five classes a day, which makes
"what do I have next?" way harder to answer than it should be. You open the app
and the answer is already sitting there: what day of the cycle it is, the class
you are in right now with a bar counting down to the bell, and what comes after
it. If you look at your watch, you get the same two answers without pulling your
phone out.

## What it does

- **Today**, with the class you are in and the one coming up.
- **The whole rotation**, which the app builds itself.
- **Take a picture of your paper schedule** instead of typing in eight classes
  by hand.
- **On your watch**, the same two answers in one glance.

## The part I figured out

The paper schedule looks like forty separate boxes, but it is really not. It is
one pattern that just keeps going. There are eight class blocks, labeled A
through H, and each day uses five of them, picking up wherever the last day
stopped. Day 1 starts at A. Day 2 starts at F. Day 3 starts at C. After eight
days you have used forty slots, which is exactly five trips through eight
letters, and you land right back on A.

So the app only stores **eight** things, not forty. If you change what class is
in Block C, it changes on all five days that block shows up. I did not have to
type the schedule in five times.

Reading the picture of your schedule uses a similar trick. Every block gets
printed five times on the page, once for each day it meets. So instead of
trusting one reading, the app collects all five and goes with whatever most of
them say. If the photo is blurry in one spot, that spot gets outvoted. The check
screen shows you the vote count for each block and warns you about any block it
could only find once.
