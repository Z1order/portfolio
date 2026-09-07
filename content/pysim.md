title: Python Sim
kind: Other
status: In development
order: 4
tagline: A place on my Mac to write Python, run it, and get help the moment it breaks.
platforms: Mac
stack: Python, pygame, Claude
icon: pysim.png
---

Python Sim is where I write Python. It is one window with my files on the left,
the code in the middle, whatever the program printed underneath, and a coach on
the right that reads what I am writing. I made it because I kept wanting to
build little games, and everything else I tried was either a plain text file
with no help in it or a giant program made for people with real jobs.

## What it does

- **Start from something that already runs.** A new file can be a small game, a
  bouncing ball, or blank. The game one opens a window with a square you move
  with the arrow keys, so there is always something to change instead of an
  empty page.
- **Press one key to run it.** The program opens in its own window. Anything it
  prints shows up under the editor, and my file saves itself, so I never lose
  work by forgetting.
- **The line that broke turns red.** When the program stops early, the exact
  line that stopped it gets marked in the editor, and the coach says what went
  wrong in normal words instead of the wall of text Python gives you.
- **A coach that is already caught up.** It reads my code after I stop typing
  and after every run. It tells me what it thinks I am building, points at the
  lines that look wrong, gives me a couple of small next steps, and asks me one
  question. I can also just talk to it.
- **It can hand me a fixed file.** If it writes one, a green button puts it in
  the editor, and undo takes it back out if I do not like it.

## The tricky part

I built the editor out of nothing. The thing I used to draw the window can put
a rectangle on the screen and put letters on the screen, and that is the whole
list. There is no box you type into. So every single part of typing is
something I had to write: where the blinking line goes, what happens when you
hold shift and drag to select, what backspace does at the very start of a line,
how far a new line should be pushed in, which words turn green and which turn
grey, and undo. Undo was the worst one. If every letter counted as its own
step, undo took a whole afternoon to get anywhere, so I had to group a run of
typing into one step and figure out where a step should end.

The other hard part was the coach, and it was hard for a reason I did not see
coming. Asking Claude a question takes about ten seconds. My first version
asked, then sat there and waited for the answer — which meant the whole app
froze every time, right in the middle of me typing. It was worse than having no
coach at all.

So the coach now thinks off to the side while the editor keeps going. That fixed
the freezing, but it made a new problem: I type faster than it thinks. If I ask
about line 3, keep working, and the answer shows up when I am on line 40, that
answer is about a file that no longer exists. Now only the newest question
counts, and anything older gets thrown away before it is ever asked. The coach
also waits six seconds after I stop typing, because if it looks the second I
pause, it always catches me halfway through a word and tells me I spelled it
wrong.
