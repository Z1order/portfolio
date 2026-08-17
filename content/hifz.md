title: Hifz
kind: Apple app
status: In development
order: 12
tagline: Helps you memorise the Quran by breaking it into small pieces and bringing them back before you forget.
platforms: iPhone, iPad
stack: SwiftUI, SwiftData
---

Hifz is for memorising the Quran. You pick a surah, and the app cuts it into
small pieces for you to say back. Then it keeps track of which verses you are
shaky on and shows you those again before you forget them.

The whole Quran is inside the app, so it works with no internet at all. That
matters, because people memorise on a prayer mat, on a plane, or in a masjid
basement with no signal.

## What it does

- **Small pieces first**, then joined together. You say one bit, then the next
  bit, then both of them in a row.
- **It practises the seams.** The app shows you the end of one piece and asks
  you for what comes next.
- **It comes back when you need it.** A verse you got wrong shows up tomorrow. A
  verse you have known for a month waits a month.
- **It changes size to fit you.** If the pieces are too easy, they get longer.
  If you keep missing one, that one gets cut smaller while the rest stay the
  same.
- **Arabic, with the meaning and the sounded-out spelling** if you want them.

## The tricky part

Where you cut matters more than how big the piece is.

My first version just counted words. Seven words, cut, seven more words, cut.
It seemed fine on paper and it was awful to actually use. Cutting by counting
lands you in the middle of a phrase, and the ending you learn is an ending that
does not exist. When you later try to recite the whole thing properly, your
brain reaches for a stopping point that is not there.

The Quran already tells you where to stop. There are little marks in the text
that show a reciter where to breathe. So Hifz cuts at those instead, and only
falls back to counting words when a stretch is so long that there is no mark
inside it.

There is a second rule that goes with it: a piece can hold several whole verses,
but it can never hold half of one and all of the next. Half of verse 3 glued to
all of verse 4 is a shape you will never see again once you know the passage.

The other thing I had to figure out was where to keep score. At first I tracked
how well you knew each piece, and that fell apart fast, because the pieces
change size as you get better. A piece you did well on last week does not exist
this week. So I score verses instead. A verse number never changes, so it can
carry a history for as long as you use the app.
