title: Jotter
kind: Apple app
status: Ready to submit
order: 16
tagline: Notes on your Apple Watch that you can actually edit after you write them.
platforms: Apple Watch (standalone)
stack: SwiftUI, watchOS
icon: jotter.png
image: jotter.png
---

Jotter is for taking notes on your Apple Watch, without needing your phone.

Apple's own Notes app came to the watch, but you cannot edit a note once you
have written it. You can only read it, tick a box on it, or pin it. I wanted
to actually write and fix notes from my wrist, so I built my own.

## What it does

- **Tap any line to edit it**, and a text box opens right there with the
  words already typed in. Dictate over them, use Scribble, or type — that one
  move is the whole difference between this and Notes.
- **The first line is the title.** There is no separate title field, so
  writing a note is just writing, not filling out a form.
- **Any line can become a checklist item**, so a shopping list and a
  paragraph of thinking are made of the same kind of line.
- **Search** shows up as its own row once you have a few notes, and it opens
  through the same box as everything else, so saying "boiler" out loud finds
  it fast.
- **A watch face complication and a Control Center button** open straight
  onto a note, so you are never hunting for the app.

## The tricky part

The Apple Watch has no text box that lets you type or edit more than one
line. That control exists on the iPhone and is turned off on the watch
entirely, so nobody, not even Apple, can build a normal editor for a long
note there.

So a note in Jotter is not one big block of text. It is a stack of short
lines, and every line fits inside the one kind of text box the watch does
have. Tap a line and a box pops up right over it with that line's words
already in it. Fix what you want, and it saves back into place.

Making the tap itself work was its own small puzzle. The watch's text box
only shows one line, so if I had just dropped one over a note, it would cut
off anything longer than a few words. And plain text reads fine but you
cannot tap into it to edit it. What I ended up doing is invisible on purpose:
draw the note normally, as text you can read across as many lines as it
needs, and lay an unseen text box over that exact same shape. Tap anywhere on
the sentence and it opens for editing, even though all you ever see is one
clean paragraph.
