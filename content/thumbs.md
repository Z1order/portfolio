title: Thumbs
kind: Apple app
status: In App Store review
order: 4
tagline: A typing speed test built for the phone, not ported to it.
platforms: iPhone (iOS 18+), portrait
stack: SwiftUI, UIKeyInput
icon: thumbs.png
image: thumbs.png
links: Site | https://z1order.github.io/thumbs-site/
---

The desktop typing test assumes ten fingers, a Tab key to restart, and a screen
wide enough to read a paragraph ahead. None of that survives the move to a
phone. Thumbs keeps the parts that actually measure typing — a three-line window
of words, per-character feedback, WPM and accuracy — and rebuilds the input
layer around two thumbs and a software keyboard.

## What it does

- **Time or word count.** 15/30/60/120 seconds, or 10/25/50/100 words.
- **Punctuation and numbers** as optional difficulty, generating real sentences
  rather than scattered marks.
- **Per-character feedback.** Wrong letters turn red, and a committed word that
  did not match keeps a red underline so the mistake stays visible.
- **Backspace across words.** Delete on an empty word steps back into the
  previous one, so a fumbled word can be repaired.
- **A haptic tap on every mistake**, because thumb typing has no other physical
  signal that a key went wrong.

## Worth knowing

The text input is a `UIKeyInput` view, not a text field. Neither SwiftUI's
`TextField` nor a `UITextField` subclass works for a typing test: both own a
string, both report edits after the fact, and neither reports a backspace on an
empty buffer — which is exactly the keystroke that steps back into the previous
word. A `UITextField` subclass cannot be forced into shape either, because
keyboard input routes through an internal field editor rather than the field's
own `insertText`.

The scoring engine owns no timer. Callers push the current instant in, which is
what lets a 60-second test be scored in a unit test without waiting 60 seconds.
