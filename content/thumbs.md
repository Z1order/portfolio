title: Thumbs
kind: Apple app
status: Live
order: 4
tagline: A typing test made for a phone instead of squished onto one.
platforms: iPhone (iOS 18+), portrait
stack: SwiftUI, UIKeyInput
icon: thumbs.png
image: thumbs.png
links: App Store | https://apps.apple.com/us/app/thumbs-typing-speed-test/id6799688303; Site | https://z1order.github.io/thumbs-site/
---

Typing tests on a computer assume you have ten fingers, a Tab key to start over,
and a screen wide enough to read ahead. None of that is true on a phone. Thumbs
keeps the parts that actually measure your typing — three lines of words, every
letter checked as you go, words per minute, and how accurate you were — and
rebuilds the typing part around two thumbs and a phone keyboard.

## What it does

- **Pick time or words.** 15, 30, 60, or 120 seconds, or 10, 25, 50, or 100
  words.
- **Turn on punctuation and numbers** to make it harder. It builds real
  sentences instead of just sprinkling in random marks.
- **Every letter is checked.** Wrong ones turn red, and a word you got wrong
  keeps a red underline so you can still see the mistake later.
- **Backspace between words.** Hitting delete on an empty word takes you back
  into the word before it, so you can fix something you messed up.
- **A little buzz every time you get a letter wrong**, because typing with your
  thumbs gives you no other way to feel that you hit the wrong key.

## The tricky part

The normal text box would not work, and I went through three of them before I
figured out why.

A typing test needs to know the exact moment you press a key. Normal text boxes
do not do that. They hold onto the text themselves, they tell you what happened
*after* it already happened, and none of them tell you when you press backspace
on an empty word. That last one matters a lot, because that is the exact key
press that should send you back into the previous word. I could not fix it by
changing a text box either, because the typing gets routed somewhere hidden
before the text box ever sees it.

So I used a much simpler piece that just reports key presses, and I built
everything else myself.

One more thing that helped: the part that keeps score does not own a clock. The
rest of the app tells it what time it is. That means I can test a 60-second
typing test without actually sitting there for 60 seconds.
