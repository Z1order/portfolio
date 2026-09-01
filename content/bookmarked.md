title: Shelved
kind: Apple app
status: In development
order: 54
tagline: Instagram, but for books. You post what you are reading, and your friends' books show up in your feed.
platforms: iPhone
stack: SwiftUI, Supabase
icon: bookmarked.png
---

Shelved is for people who read a lot and want to share it. You post the books
you are reading and the ones you have finished, with a few sentences and how far
you have gotten. You follow your friends, and their books show up in your feed.

It used to be called Bookmarked. It is still being built. You can make a real
account now, search for any real book and put it on your shelf, and the shelf
saves. The posts in the feed are still made up ones I wrote, because the posting
screen — where you write about a book and rank it — is the next thing I am
building.

## What it does

- **A feed made of books.** Every card is one book — the cover, who posted it,
  and what they thought of it.
- **No star ratings.** Stars never mean the same thing twice. When you finish a
  book, Shelved asks you which of two books you liked better, a few times over,
  and slots the new one into the right spot on your list. Your score comes from
  where it landed.
- **Any real book.** You can search by title, type in the number on the back
  cover, point the camera at the barcode, or just type the book in yourself if
  it is not anywhere.
- **Posting where you are, not just what you finished.** You can put up a book
  the day you start it, again halfway through, and again at the end.
- **A library on your profile** that draws your books as spines standing on
  shelves, best at the top, like a shelf in a bookstore.
- **A tab bar I drew myself**, with a round orange button in the middle for
  posting. The one iPhone gives you for free looks like every other app.
- **Tapping a cover grows it into the whole page** instead of sliding a new
  screen over the old one.

## The tricky part

I picked a font called Fraunces for the app, because it is a serif font that
still looks a bit fun. Fonts like that usually come as one file that can be any
thickness you want, from thin all the way to very bold, like a dial you turn.
That sounds better than having a separate file for each thickness. It is not.

The iPhone will only ever use the one setting the file starts on. So I put the
font in, and every title in the app came out the exact same medium thickness.
The big headings and the small labels looked identical. Nothing told me
anything was wrong — no error, no warning, and the font was clearly working. It
just quietly ignored every thickness I asked for.

The fix was to go get four separate files, one for each thickness I wanted, and
call each one by its own name instead of asking for the dial. Then I built a
tiny screen inside the app that puts all four side by side, so I can look at it
with my own eyes and see that they are actually different. That screen is not
for anyone else. It is there because this is the kind of mistake you cannot
catch by reading the code.

The colors had a similar trap. The app is warm tan and cream, and the main
orange looked great on it — until I measured it. Orange on tan is too close in
lightness to read at small sizes, so anyone with weaker eyesight would have
struggled. Now the orange only fills buttons and big shapes, and any text in
that color uses a darker version of it.

Book search had a trap of its own. I get the books from Google, and you are
allowed to ask without signing up for anything, which was great until search
started coming back empty for no reason. It turned out that everyone in the
world who asks without signing up is sharing one daily allowance, and by the
afternoon other people had used it up. Nothing was broken on my end. My app just
looked like it could not find a single book.

So now every search has a backup. If Google says no, the app quietly asks a
second library called Open Library instead, and you never find out the first one
was busy. It waits a couple of seconds and tries once more before it gives up,
because sometimes the allowance frees up that fast.
