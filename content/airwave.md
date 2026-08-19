title: Airwave
kind: Apple app
status: Ready to submit
order: 30
tagline: Lets you and your friends listen to the same music at the same second, on your own phones.
platforms: iPhone
stack: SwiftUI, CloudKit, MusicKit
icon: airwave.png
image: airwave.png
links: Site | https://z1order.github.io/airwave-site/
---

Airwave turns your phone into a shared radio station. One person starts a
jam, loads in a playlist, and reads out a six-letter code. Everyone who types
that code in hears the exact same song at the exact same second, and anyone
can add to the queue while it's playing.

## What it does

- **A shared code** gets everyone listening in sync, like tuning into the
  same radio station instead of sending audio back and forth between phones.
- **Import from Apple Music or Spotify**, or just search for a song directly
  — no account needed for search.
- **Anyone can add to the queue**, but only the person who started the jam
  can skip a track.
- **Works without a subscription.** If the host doesn't have Apple Music,
  everyone hears 30-second previews instead of full songs, so nobody in the
  jam needs a subscription to join in.

## The tricky part

Nothing is actually streamed between phones — that's not something Airwave
is even allowed to do. Instead, every phone plays the song on its own and
figures out exactly where it should be in the song using one shared piece of
information: the exact moment the current song started. That's the same
trick real radio uses — everyone tunes to the same clock instead of passing
the actual sound to each other. It's also why someone joining a jam that's
already halfway through a song lands in the right spot immediately, instead
of starting the song over.

The other tricky part was making sure two people editing the queue at the
same instant — like a guest adding a song right when the host skips a track
— don't accidentally erase each other's change. Every edit gets applied on
top of whatever the very latest version already says, and retries itself if
someone else's edit snuck in first, so both changes survive.
