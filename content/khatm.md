title: Khatm
kind: Apple app
status: In development
order: 46
tagline: Splits a full reading of the Quran between a group, so nobody doubles up and nothing gets missed.
platforms: iPhone
stack: SwiftUI, SwiftData, CloudKit
icon: khatm.png
---

When a family reads the whole Quran together, they split it into thirty parts
and hand them out. Right now that happens in a WhatsApp group, and it goes
badly. Someone says "I'll take 14", then forty messages later someone asks
whether anyone has done 22, and nobody can answer. Two people read the same
part. Three parts never get taken at all.

Khatm is one screen everyone can see: a grid of thirty boxes. Empty means free,
tinted with a name means taken, filled in means read. One person starts it and
everyone else joins with a six-letter code.

## What it does

- **The same picture for everybody.** Not a list of what you took — the whole
  thing at once. Watching it fill up is the point.
- **Giving a part back is a normal thing to do.** It is a button right there,
  not something buried in a menu. The usual way one of these dies is one person
  sitting on three parts they are not going to read, and every week that goes
  by makes saying so harder.
- **A dedication, asked for first.** Most of these are read for someone who
  died. So the form asks who it is for before it asks anything else, and it
  sits at the top of every screen in a nice serif font.
- **Two notifications, ever.** One reminder two days before the deadline, and
  only if you are holding something. One message when the whole thing is
  finished. No app should ever tell one person that another person has not read
  yet.
- **Where each part starts** — the surah, the verse and the page number. That is
  the one line you need before you open your own copy. The app does not contain
  the Quran and never shows you a verse.

## The tricky part

Two people can tap the same part at the same second, and only one of them can
have it.

Normally you would need a server to sort that out, and I do not have one. This
app runs entirely in the readers' own iCloud. So I had to find a way for two
phones to disagree and settle it without anything in the middle.

The trick is that every part gets a name built from the numbers, not a random
one. Part 14 of this reading is always called the same thing, on every phone.
So when two people claim it at once, they are both trying to make something
with that exact name, and iCloud only lets the first one exist. The second gets
told no. There is no lock and no referee — the name being taken *is* the
answer. The loser's screen then says "Amina just took juz 14" instead of some
error, which is what a person actually wants to know.

The bit that took me longest was working out which taps to give up on and which
ones to keep trying. Losing a claim is fine — the part belongs to someone else
now, and trying again would be taking it off them. But tapping "finished" is
different. That is your own part, and you already did the reading. So if that
tap fails, the app keeps trying until it lands, even if you tapped it in a
basement with no signal and the phone only got out forty minutes later. A
"finished" tap is never thrown away.

I also could not test any of this properly at first, because it really wants two
phones on two different iCloud accounts, which meant I never tested it at all.
So I wrote a fake iCloud that follows the same rules and lives in memory. Two
copies of the app pointed at one fake is the same as two phones, and now the
most important thing in the app has actual tests.
