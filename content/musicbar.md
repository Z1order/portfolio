title: MusicBar
kind: Apple app
status: In development
order: 34
tagline: A tiny menu bar player for your Mac that shows and controls whatever music is playing.
platforms: Mac
stack: AppKit, Swift
---

MusicBar sits in your Mac's menu bar and shows whatever song is currently
playing, from basically any app — not just Apple Music. You can play, pause,
skip, and search for a new song without ever switching over to the actual
music app.

## What it does

- **Shows what's playing**, with the artwork, right in the menu bar, no
  matter which app is actually playing it.
- **Play, pause, skip and adjust volume**, all from the menu bar.
- **Search** your library or the catalog and start playing something new
  without opening another app at all.

## The tricky part

macOS doesn't really offer a normal, public way for an app to ask "what song
is playing right now" across every other app on the system. Apple Music and
Spotify can both be asked directly through an old scripting system, but that
only works for those two specific apps — anything else playing music, like a
podcast app or a browser, is invisible to it.

So MusicBar uses a second approach behind the scenes to see across every
app, and only falls back to the old two-app-only method if that doesn't work
on someone's Mac. Neither one is normally simple to set up from inside an
app, so getting them to run automatically, quietly, and hand off to each
other without the person using the app ever noticing was most of the actual
work here.
