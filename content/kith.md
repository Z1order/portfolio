title: Kith
kind: Apple app
status: Ready to submit
order: 27
tagline: Tracks who you've actually talked to lately, so nobody falls through the cracks.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: kith.png
image: kith.png
links: Site | https://z1order.github.io/kith-site/
---

Kith is Streak's idea — tracking what you actually did instead of what
you're supposed to do — pointed at people instead of habits. You talked to
your uncle, so you open the app and tap his name. That's the whole thing. The
app answers exactly one question: who have I not talked to in too long?

## What it does

- **A list of everyone you're keeping up with**, sorted by who you're most
  overdue to talk to.
- **One tap logs "we talked today"**, with an undo button if you tap the
  wrong person.
- **You pick how often per person** — weekly for your best friend, yearly for
  a distant cousin — and the app works out on its own who counts as overdue.
- **A red, yellow or green dot** for everyone, so you can see who needs a
  message at a glance instead of reading through a list.
- **Add people from your contacts**, without giving the app access to your
  whole contacts list — you pick exactly who gets added and nothing else gets
  shared.

Someone you just added with no history yet counts as overdue right away —
which makes sense, since the reason you added them is that it had already
been too long.

## The tricky part

Nothing in this app is planned ahead of time — there's no calendar, no
reminders you set up in advance. Every single thing you see, like whether
someone is overdue and how the list is sorted, gets worked out fresh from the
plain list of "I talked to this person on this date" entries. That sounds
small, but it means there's no separate "status" stored anywhere that could
quietly drift out of sync with what actually happened. If the rule for what
counts as "too long" ever needs adjusting, I only have to change it in one
place, and every screen in the app updates itself automatically.
