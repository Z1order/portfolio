title: Hearth
kind: Apple app
status: In development
order: 55
tagline: A remote control for a whole house that runs on a phone and costs nothing every month.
platforms: iPhone
stack: SwiftUI, HomeKit, Swift
icon: hearth.png
---

Hearth puts a whole house on one phone. Every room gets its own screen with the
lights, shades, thermostat, doors, music and cameras that are in it, and the
front page shows what is playing and the buttons I press most. It is for a
family that already has smart home gear from a few different companies and is
tired of opening five apps to turn things off at night.

## What it does

- **A screen for each room.** Lights and dimmers, shades, the thermostat, locks
  and the garage, whatever music is playing in there, and the cameras.
- **Six systems in one place.** Apple Home, Sonos, Spotify, UniFi, eero and
  Control4 all show up together. Once a light is on the screen it does not
  matter which company it came from.
- **I arrange it myself.** Drag a tile into a different room, rename it, hide
  the ones nobody needs, and pin the good ones to the front page.
- **No monthly fee, ever.** There is no Hearth company in the middle. My phone
  talks to each system straight over the Wi-Fi, or signs in to the account I
  already pay for, so there is nothing left to charge me for.
- **No voice and no AI, on purpose.** Hearth is a remote, not an assistant.
- **A pretend house is built in**, so the app can be opened and pressed without
  owning any of this.

## The tricky part

The hard part was finding the gear in the house in the first place.

Most home gear expects to be found by shouting. A phone sends one message to
the whole network that means "is anybody out there?", and everything listening
shouts back. That is how the Sonos app finds speakers in about a second. But an
iPhone app is not allowed to send that message unless Apple hands it a special
permission, and an ordinary app does not have one. So my app was standing in a
room where it was not allowed to speak.

What it does instead is knock on every door. A home network has 254 addresses
in it. Hearth asks all 254 of them a short question — are you a Sonos speaker?
are you a Control4 controller? — twenty-four at a time, and anything that has
not answered in two and a half seconds gets skipped. The whole sweep takes a
few seconds instead of one. It is slower, but it also works on the routers that
block the shouting, and a lot of them do.

Control4 had a surprise in it. I ask an address "are you the controller?" and
more than one box says yes. It turns out every Control4 controller in a house
answers that question exactly the same way, even the ones that are not the one
in charge. Nothing in the answer tells them apart. So the app stopped trying to
be clever and just shows me the list to pick from.

The other thing that took a while was rooms. All six systems have their own
idea of what a room is called. Apple Home calls it the family room, Sonos calls
the speaker sitting in that same room the living room, and Control4 has two
more names for it. When I trusted them, the app showed me the same room three
times with a third of the stuff in each one. So Hearth keeps its own list of
rooms and treats every system's names as a first guess. When I move a light or
rename it, that is saved in my list only — it never gets sent back, so nothing
I do in Hearth changes what anyone else's app looks like.
