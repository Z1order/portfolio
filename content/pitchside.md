title: Pitchside
kind: Web
status: In development
order: 2
tagline: Live soccer scores and tables, plus a daily guess-the-player game.
platforms: Web
stack: HTML, CSS, JavaScript, Python
---

Pitchside is a web page that shows live soccer scores for 14 leagues and cups,
with the tables, the top scorers and a daily game called Mystery Player. It
runs on my own computer. There is no account, no app to install and no key to
sign up for. I made it because I wanted the scores app I liked, without the ads.

## What it does

- **Every match today, in one place.** Each league gets its own group, with a
  count of how many games are live right now. Under each score it lists who
  scored and when, and marks red cards. A strip at the top lets me flip to
  other days.
- **Click a match for more.** A timeline of goals, cards and subs. The stats,
  like possession and shots. The lineups, drawn on a little pitch in the
  formation each team is actually playing, with the bench underneath.
- **Tables and top scorers.** The standings for each league, with the
  Champions League and relegation spots colored in. The top scorers list is
  built from every club's squad.
- **Mystery Player.** One player a day from the five biggest leagues, and the
  same one for everyone. You type a guess, and six boxes tell you if you got
  the nation, league, club, position, age and shirt number right. Age and
  shirt number show an arrow for higher or lower. You get eight guesses, a
  hint with the initials after four, and the height after six. Your streak is
  saved in the browser.
- **It keeps itself fresh.** The page refreshes every minute, and a little
  ring in the corner counts down to the next one.

## The tricky part

The scores come from the same feed ESPN's own website reads. But there is a
rule in every web browser that a page is not allowed to read data from a
different website unless that website says it is okay. Most of ESPN's feed
says okay. The one list of all the clubs in a league does not. So I could not
ask for the clubs directly. Instead I read the league table, which does say
okay, and pull the clubs out of that. The table has every club in it anyway.

The same rule is why Pitchside lives on my computer and not on a shared link.
The kind of page I can publish is locked down so it cannot read other
websites at all. A page served from my own Mac can, so that is where it runs.
Double-clicking one file starts a tiny server and opens the page.

Mystery Player had a different problem. I wanted everyone to get the same
player each day, the way Wordle works, but there is no server picking one and
sending it out. So the page turns today's date into a number and feeds it to
a pretend-random number maker that always gives the same answers for the same
starting number. Every copy of the page does the same math and lands on the
same player. The first version picked from all 2,749 players, which meant a
lot of backup goalkeepers nobody has heard of. Now it ranks players by how
much they have played and scored, and only the top 500 can be the answer.
