title: WidgetBar
kind: Apple app
status: In development
order: 52
tagline: A small dock that holds my other floating Mac widgets and pops them out when I click one.
platforms: Mac
stack: Swift, SwiftUI, AppKit
---

I kept making little floating widgets for my Mac — one for music, one for
email, one for homework — and my screen filled up. WidgetBar is a dock for
them. It holds them all in one small strip, and clicking one sends it out onto
the desk. Clicking it again puts it away.

## What it does

- **Finds my widgets on its own.** It looks for the ones I have installed
  instead of me listing them somewhere, so a new one I make shows up without
  changing WidgetBar at all.
- **One click puts a widget out or away**, and the dock shows how many are
  currently out.
- **Comes back with a keyboard shortcut**, like the rest of them.

## The tricky part

Every one of these widgets is a separate app. None of them knows the others
exist, and none of them is in charge. So when two of them opened in the same
corner of my screen, they just sat on top of each other, and I had to drag one
off the other every single time.

I could not fix that from one place, because no app is allowed to shove another
app's window around. What I did instead was give every widget the same small
rule: whenever you land somewhere — you just opened, or I just finished
dragging you — look at where the other widgets are and step aside if you are
covering one. Each app only ever moves itself, and the pile sorts itself out.

I added one more thing while I was in there. If I drop a widget close to
another one, it snaps flush against it with a small gap, and lines up its
edges if they were nearly straight already. That way a screen full of these
looks tidy without me measuring anything.
