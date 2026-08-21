title: Dispatch
kind: Apple app
status: Ready to submit
order: 38
tagline: Lets you talk to Claude Code and Claude chat from your Apple Watch, with your Mac doing the actual work.
platforms: Apple Watch (standalone), Mac
stack: SwiftUI, watchOS, TLS
icon: dispatch.png
image: dispatch.png
links: Site | https://z1order.github.io/dispatch-site/
---

Dispatch puts Claude Code and Claude chat on your wrist. You type a prompt on
your watch, and it looks and feels like the desktop app — a list of
conversations, the answer streaming in, tool calls showing up as they happen.
Claude Code itself still runs on your Mac, because that's the only place it
can read files and run commands. Dispatch just gives you a window into it
from your wrist.

## What it does

- **A watch app that talks to your Mac.** A small program on your Mac runs
  the real work and streams the result back to the watch as it happens.
- **Locked to one watch and one Mac.** Nothing else can connect, even on the
  same Wi-Fi.
- **Works offline for chat**, if you turn that on, by talking to Claude
  directly instead of going through your Mac.

## The tricky part

watchOS can't read files or run terminal commands, so there was no way to
put Claude Code on the watch by itself. The only option was to have the
watch send a message to the Mac and let the Mac do the real work.

That meant the connection between them had to be locked down hard, because
it can run commands on your computer. So every message the watch sends is
signed with a key that's generated inside the watch's own security chip and
can never be copied out, even by me. If someone stole the watch and tried to
copy the connection to a different phone, the signature wouldn't match and
the Mac would refuse it. And when you first pair the watch to your Mac, the
watch checks a fingerprint of the Mac's identity before it ever sends
anything secret, so even a stranger's computer pretending to be yours can't
trick it.
