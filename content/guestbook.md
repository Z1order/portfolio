title: Guestbook
kind: Apple app
status: In development
order: 39
tagline: A ledger for having people over, so you remember who can't eat nuts and what you already served them.
platforms: iPhone
stack: SwiftUI, SwiftData
icon: guestbook.png
---

Guestbook is for people who host a lot. You write down who came, what you
cooked, and how it went — in about a minute, right after everyone leaves.
Next time those people are coming over, it tells you the stuff you'd
otherwise have to remember yourself: who can't eat what, and what you
already served them.

## What it does

- **Guests, not dinners.** A guest can be a whole family, like "the
  Kapoors," which is one row even though four people show up. That's how
  invitations actually work.
- **Everyone's restrictions merged into one card** the second you pick who's
  coming. If even one person at the table is vegetarian, the whole card says
  so — it never averages that away.
- **A quiet flag if you're about to repeat a dish**, and another one if a
  dish's notes mention something a guest can't eat, even if the dish's name
  gives nothing away.
- **Closing out an evening** takes one tap per dish — loved it, fine, skip
  it — plus one optional line about how it went.

## The tricky part

The hard part wasn't storing the data. It was making sure the app never
tells you something is fine when it isn't, and never nags you about
something that doesn't matter.

So the allergy and repeat flags never block anything — they just show up
quietly, because I know things the app doesn't, like that I'm leaving the
nuts out tonight. And the flags don't just check a dish's name; they also
read its notes, because a dish called "shahi korma" doesn't mention nuts by
name, but "cashew paste, blended smooth" does. Getting that scan to catch
the real risky word without also going off on things that just sound
similar took a lot of trial and error.
