title: EmailBridge
kind: Other
status: In development
order: 3
tagline: I email Claude from my Apple Watch, and the answer comes back as mail that buzzes my wrist.
platforms: Apple Watch, Linux server
stack: Python, Claude
---

I do not have an iPhone. My watch is set up through my parents' phone, which
means most apps and shortcuts cannot go on it at all. Mail is one of the few
things that does work. So EmailBridge lets me talk into my watch to write an
email, and a small computer in the cloud reads it, asks Claude, and mails the
answer straight back into the same thread.

## What it does

- **Two modes**, picked by the first word of the message: ask Claude a
  question, or have Claude do actual work on the server.
- **Replying in the thread keeps going.** I only need the starting word once.
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

The other half was that my Mac cannot be the one doing this. It sleeps, and it
is not always at home with me. So the part that waits for mail lives on a small
computer in the cloud that never sleeps, checking for new mail every twenty
seconds. Answers take about a minute, which is roughly how long it takes me to
put my arm down.
