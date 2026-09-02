title: MusicBar
kind: Apple app
status: In development
order: 34
tagline: A tiny menu bar player for your Mac that controls whatever is playing, one app at a time.
platforms: Mac
stack: AppKit, Swift
---

MusicBar sits in your Mac's menu bar and shows whatever song is currently
playing, from basically any app — not just Apple Music. You can play, pause,
skip, and search for a new song without ever switching over to the actual
music app.

It also lists every app that is making noise right now, so you can turn one
of them down without touching the others.

## What it does

- **Shows what's playing**, with the artwork, right in the menu bar, no
  matter which app is actually playing it.
- **Play, pause, skip and adjust volume**, all from the menu bar.
- **Lists every app making sound.** A game, a video in your browser and your
  music can all be going at once, and each one gets its own row. Music and
  Spotify get a volume slider. Everything else gets a mute button. Clicking
  the name brings that app to the front.
- **Shows where the sound is going**, like your speakers or your AirPods.
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

Turning one app down was harder than it sounds. Your Mac has one volume for
the whole computer, not one per app. Apple Music and Spotify will turn
themselves down if you ask them nicely, but nothing else will, and there is
no setting anywhere for "make this one app quieter."

What I found is that macOS does let an app record another app's sound, and
when you set up that recording you get to say whether the app should still
be heard while you listen. So MusicBar starts a recording it never actually
listens to, purely to say "no." The app goes silent. Stopping the recording
brings it back.

That worked, and then browsers broke it. A browser does not make its sound
itself — it hands the job off to little hidden helpers, and there can be
several at once. Silencing the one that was playing left the others audible,
so a muted tab would come back the moment you opened a new one. MusicBar now
silences every helper the browser owns, and checks again when new ones show
up.
