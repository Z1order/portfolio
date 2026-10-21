title: TaskBar
kind: Apple app
status: In development
order: 51
tagline: A floating checklist for homework and chores that stays on top of everything on my Mac.
platforms: Mac
stack: Swift, SwiftUI, AppKit
---

TaskBar is a little checklist that floats above whatever else is on my screen,
so my homework is still in front of me while I am doing it. I made it because a
to-do list I have to go and open is a to-do list I forget about.

## What it does

- **Add a task and press return.** The box keeps the cursor, so I can type in
  five things in a row without clicking again.
- **Click the circle to finish something.** It crosses out, drops to the
  bottom, and plays a small sound. The last one of the day gets a better sound.
- **Daily tasks come back every morning**, like making my bed and packing my
  bag. Finished one-time tasks clean themselves up overnight.
- **My homework adds itself.** Every afternoon it checks my school's homework
  site and puts anything new on the list, with the class and the due date. If I
  already turned something in, it comes in already ticked off.
- **It reads my teachers' homework documents too.** Some classes keep the real
  list in a shared document and color a line yellow when that work is
  actually assigned. The sync only takes the yellow lines.
- **It warns me when homework is probably missing.** A couple of my classes
  give work every single time they meet. If one of them met today and nothing
  showed up, I get a task telling me to go and look for it.
- **My homework shows up on my watch too.** The homework rows get copied into
  a Reminders list that goes through iCloud, so the same list is on my watch
  and in the Calendar app. Tick one off on the watch and it ticks off in
  TaskBar. Tick it in TaskBar and the reminder finishes. The night before
  something is due, Calendar gives me a nudge at seven.
- **Collapses into a small dot** with the number of things left in it.

## The tricky part

I wanted a window that sits on top of everything but never takes over. If I am
typing an essay and the checklist grabs the keyboard, I have ruined the thing I
was trying to help.

macOS can make a window like that, but there is a catch nobody warns you about:
a window that never becomes the active window also never gets told about
clicks the normal way. My first version looked perfect and did absolutely
nothing when I clicked it.

Dragging it around was worse. The usual way to drag something is to ask how far
the mouse has moved since it was pressed down. But here the window itself is
moving with the mouse, so the mouse never gets very far away from where it
started — the window keeps catching up to it. The drag would go a few pixels
and stall. The fix was to stop asking about the window at all and just track
where the pointer is on the whole screen, then move the window by that
difference each time.

The reminders part had its own surprise. When I make a reminder, Apple gives
it a name tag so I can find it again later. But a few minutes after it syncs
to iCloud, that tag quietly changes. My first version went looking for every
reminder by its old tag, found none of them, and decided I had deleted all
fifty-eight of them by hand. Now it uses a second tag the server hands out,
which stays the same forever.
