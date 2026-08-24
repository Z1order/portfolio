title: SelfChatBot
kind: Other
status: In development
order: 2
tagline: I text myself a message from any device, and Claude answers in the same chat.
platforms: Mac, iPhone, Apple Watch
stack: Python, SQLite, AppleScript
---

In Messages you can send texts to yourself, and they show up on every device
you own. SelfChatBot watches that one conversation on my Mac. If I start a
message with a short command, it hands what I wrote to Claude and posts the
answer back into the same chat, so I can read it on my watch a minute later.

## What it does

- **Two modes.** One asks Claude a plain question. The other lets Claude
  actually work on my projects on the Mac.
- **Remembers the conversation** in each mode, so I can ask a follow-up
  without explaining everything again, until I tell it to start over.
- **Ignores every other conversation.** It only ever reads the chat I have
  with myself.

## The tricky part

Two things nearly stopped this.

The first was permission. Messages keeps everything in a file that macOS
protects, and you have to go into settings and allow a program to read it. I
did that, and it still would not work. It turned out the thing I had given
permission to was not really the program — it was a small stand-in that hands
the job off to the real one. macOS was watching who actually opened the file,
not what I had typed into the settings window. Once I pointed the permission at
the real program, it worked first try.

The second was that the bot kept talking to itself. Its answers land in the
same conversation it is watching, so it would read its own reply, treat it as a
new message, and answer that too — forever. Now every reply starts with a
little symbol, and anything starting with one of those gets skipped. It is a
silly fix for a problem that felt very serious at 11pm.
