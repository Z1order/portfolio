title: MailBar
kind: Apple app
status: In development
order: 50
tagline: A small bar that floats on my Mac screen and shows the unread email waiting for me.
platforms: Mac
stack: Swift, AppKit, AppleScript
---

MailBar floats on top of everything on my Mac and shows the email I have not
read yet. It makes a small sound when something new arrives. It is for anyone
who keeps missing mail because their inbox is buried behind ten other windows.

## What it does

- **Shows the unread mail**, who it is from and the subject, without opening
  the Mail app at all.
- **Pings when something new lands**, and shows a little card so I notice.
- **Mark as read, flag, or open a message** right from the bar.
- **Shrinks into a small dot** when I want it out of the way, and comes back
  with a keyboard shortcut.

## The tricky part

MailBar does not talk to my email company at all. It asks the Mail app that is
already on my Mac, using an old built-in way of asking apps questions. That
sounds easy, and then it is not.

The obvious way is to grab all the unread messages first, and then ask that
pile who each one is from. That fails every time. Once you grab the pile, it is
just a list of things you already picked up, and Mail will not answer questions
about it anymore. You have to ask the question in one go instead: "who are the
unread messages from?" So MailBar asks five separate questions — the senders,
the subjects, the dates, and so on — and lines the five answers up like
columns. If mail arrives in the middle of all that asking, the columns end up
different lengths, so it counts them and starts over the slow way when they do
not match.

The other surprise was time. Mail hands back its dates as if the whole world
were in my time zone, so every message looked hours off until I shifted them
back myself.
