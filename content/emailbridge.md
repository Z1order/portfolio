title: EmailBridge
kind: Other
status: In development
order: 3
tagline: I email Claude from my Apple Watch, and the answer comes back as mail that buzzes my wrist.
platforms: Apple Watch, Mac
stack: Python, Claude
---

I do not have an iPhone. My watch is set up through my parents' phone, which
means most apps and shortcuts cannot go on it at all. Mail is one of the few
things that does work. So EmailBridge lets me talk into my watch to write an
email, and a computer that is always awake reads it, asks Claude, and mails
the answer straight back into the same thread.

## What it does

- **I just write the question.** The inbox is only used for this, so anything
  I send it goes straight to Claude. There is no special word to remember
  while I am talking into my watch.
- **A second mode for real work.** Starting the message with "claude code"
  sends it to go do the task on the computer instead of only answering.
- **Replying in the thread keeps going.** It remembers what we were already
  talking about, so I can ask a follow-up without explaining again.
- **Only answers me.** Mail from anyone else is written down in the log and
  ignored.

## The tricky part

The whole point was to get an answer on my wrist, and my first idea did not do
that. I already had a version that used Messages, and it worked, but a message
I send to myself never buzzes my own watch. It just quietly appears. I had to
keep checking, which is worse than not having it.

Real incoming email is different. It comes from outside, so the watch treats it
like anything else and taps me. Once I noticed that, the whole design changed:
the answer goes out as a normal email to my own address, and the buzz comes for
free.

The other half is that something has to sit there watching the inbox all day,
and it cannot be me. I built it so it can live on a small computer in the cloud
that never sleeps. Right now it runs on my Mac instead, and it starts itself
back up on its own if it ever stops. Either way it checks for new mail every
twenty seconds. Answers take about a minute, which is roughly how long it takes
me to put my arm down.
