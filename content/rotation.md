title: Rotation
kind: Apple app
status: Ready to submit
order: 24
tagline: Logs what you actually wear, and shows you what that adds up to.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: rotation.png
image: rotation.png
links: Site | https://z1order.github.io/rotation-site/
---

Everyone thinks they wear most of their closet. Almost nobody actually does.
You can't notice that from just looking in your closet, because the clothes
you wear all the time are the ones you see all the time, and the ones you
never wear are shoved in the back where you stopped looking. Rotation doesn't
organize your closet or plan outfits — it just logs what you put on, and then
shows you the real shape of it.

## What it does

- **Cost per wear.** A $320 jacket worn twice cost $160 each time you wore
  it. A $30 sweater worn ninety times cost 33 cents. This is the number that
  actually changes how people shop.
- **What's gathering dust**, sorted by how much it cost — not by how long
  it's been sitting there. A cheap shirt you haven't worn in a year isn't
  interesting. An expensive coat is.
- **How wide your rotation actually is** — like "your five most-worn things
  make up 56% of everything you've worn, out of 29 things you own."
- **The colors you actually reach for**, and outfit combos you keep repeating
  without ever deciding to.

## The tricky part

An app like this only works if logging an outfit takes seconds, because a log
that takes a minute gets used for a week and then forgotten, and a week of
data can't tell you anything real. So only one thing is required to log a
fit: which clothes you wore. Everything else — a rating, a note, a photo — is
optional, and the date just defaults to today.

The other detail I had to get right was the order clothes show up in when
you're picking what you wore. I sort by what you wear most, which sounds
simple, except your most-worn shirt is also the one you probably wore
yesterday — and almost nobody wears the exact same shirt two days running. So
anything worn in the last day drops to the bottom of the list instead of
sitting at the top, which makes the picker actually feel like it's guessing
right instead of constantly showing you what you just took off.
