title: ClassBar
kind: Apple app
status: In development
order: 53
tagline: A floating card on my Mac that shows my school day, and a helper that sends the plan to my watch.
platforms: Mac, Apple Watch
stack: Swift, SwiftUI, AppKit, WebKit, EventKit, Claude
---

ClassBar sits on top of everything on my Mac and shows my school day in order —
every class, when it starts, which teacher and which room. I made it because I
was checking two different school websites every morning to answer one question,
which is what class do I have next.

It grew. Now it also puts my school day and my homework plan on my Apple Watch,
and it taps my wrist a few minutes before each class with where to go.

## What it does

- **The whole day, in order.** Each class with its time, its block letter, the
  teacher and the room. Lunch, advisory and clubs are in there too, wherever the
  school actually put them that day.
- **Marks the class I am in right now**, and the one right after it.
- **One line that tells me what to do.** Above the list it says things like
  "Leave at 9:10 for Band" or "Free until 4:00, then Algebra homework". On days
  a class needs my PE kit or my instrument, the leave line says to pack it.
- **Switches to tomorrow on its own.** Once the last class of the day is over,
  the card shows the next school day instead. So looking at it after dinner
  tells me what to pack, and looking at it in the morning tells me what I have.
- **Arrows at the bottom look further ahead**, one school day at a time. They
  skip weekends and holidays, so there is never an empty day to page past. A
  **Now** button jumps back to today, and it goes back by itself after a couple
  of minutes if I forget.
- **My activities are on the card too.** My mom keeps tennis and piano and the
  rest in a shared calendar on her phone. The card mixes them in between the
  classes, so at 6pm it can say tennis is next.
- **The school day goes to my watch.** A helper writes the next two weeks of
  classes into a calendar that syncs through iCloud, with the room on each one.
  My watch shows them like any other appointment.
- **It plans my homework for me.** It takes the homework from TaskBar and fits
  it into the free time I actually have that evening, as blocks on the
  calendar. Homework lands the night before it is due, like real life. A test
  gets three study sessions on different days instead of one long one.
- **It taps my wrist before each class.** A few minutes before anything starts,
  I get a short line with what is next, which room, and the one homework thing
  worth knowing for that class.
- **An evening recap at 8:45.** One line with tomorrow's shape, what is due,
  and what is still left tonight. On Sunday it covers the whole week. At 9:30
  it tells me to wind down and what to pack.
- **I can talk back from my watch.** Emailing "done algebra 3.3" ticks it off,
  "skip tonight" moves things, and "what's the next test" gets an answer in a
  second. Claude looks over tomorrow each evening and can suggest up to three
  small changes to the plan.
- **Shrinks into a small bubble** with the rotation day in it, and comes back
  with a keyboard shortcut.

## The tricky part

Nothing my school gives me knows my whole schedule. Two different websites each
know half of it.

The schedule page knows **when**. It has every date of the year, which day of the
rotation it is, and the real bell times — including all the strange days, like
the late starts and the assembly days and the first day where every class meets
for fifteen minutes. I could not have worked those out from a pattern. They just
have to be read.

The class website knows **what**. It has my eight classes and my teachers on it.
But it has no calendar at all, so it never says when any of them meet. The only
place that shows up is inside the name of each class, which looks like this:
`x.F.F.x.F.F.x.F`. Eight spots for the eight days of the rotation, and the letter
is the block. Once I noticed that, the two halves clicked together. The schedule
page says "Block F at 10:35" and the class website says Block F is English.

Then there was the part where the school's site would not answer me at all. It
sits behind one of those "checking your browser" screens, and anything that is
not a real browser gets turned away. My app was not a real browser, so it kept
getting the door shut on it. What works is opening the page in a hidden window
first and letting that screen run its check, then asking for the file from inside
that window, where it counts as a browser and gets let through.

## The watch part

I do not have an iPhone, and my watch is set up through my parents' phone. That
means I cannot put my own app on it at all. The only apps on it are the ones
that come with it. So the Mac cannot talk to the watch directly. It has to leave
notes somewhere the watch already looks.

The watch already looks at Calendar and Reminders, and both of those read from
iCloud. So the helper on my Mac writes events into a calendar and reminders into
a list, iCloud carries them over, and the watch shows them as if I had typed
them in myself. That is the whole trick. A calendar turned out to be a way to
send messages.

The timing was the hard bit. If I want a buzz four minutes before class, the
Mac has to put an alarm on the event and iCloud has to carry it to the watch
before that time arrives. My first version set the alarm ninety seconds ahead.
The Mac buzzed every time. The watch never did, because by the time the alarm
got there it was already in the past, and an alarm that is already in the past
does nothing. Four minutes ahead reaches both. I only found that by sitting
there with the watch on and waiting.

The other thing I got wrong was letting the nudge change the name of the class
on the calendar so the words would show up on the watch. That worked once. Then
the next nudge read the calendar back, saw a class called "Go to room 310 for
English" and got confused about what the day looked like. Now the words go in a
reminder instead, and the calendar keeps the real class names.
