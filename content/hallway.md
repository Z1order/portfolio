title: Hallway
kind: Other
status: In development
order: 6
tagline: A webcam in the hallway that beeps when someone is walking toward my door.
platforms: Mac
stack: Python, YOLOv8, OpenCV
---

Hallway is a small program that watches a webcam pointed down the hallway
outside my room. When someone shows up, it beeps. When someone is actually
walking toward my door, it beeps a lot louder. Everything runs on my own Mac,
so no video ever goes anywhere.

## What it does

- **Three different sounds.** A soft beep means a person showed up. A chime
  means someone reached the top of the stairs. A loud beep means someone is
  coming straight at the door. If two happen at once, only the most important
  one plays.
- **It spots people, not motion.** It uses a small program that has already
  learned what people look like, so a moving shadow or a coat on a hook does
  not set it off.
- **I draw the stairs spot myself.** In the preview window I drag a box over
  the floor at the top of the stairs, and it remembers it. It checks where
  your feet are, not your head, because feet are what stand on the floor.
- **It keeps going.** If the camera gets unplugged and plugged back in, it
  finds it again on its own.

## The tricky part

Seeing a person is the easy part. The hard part is telling "walking toward
me" apart from "walking past." A camera only sees a flat picture, so it
cannot measure how far away you are. What it can see is how big you look.
When someone walks toward the camera, the box around them gets taller, the
same way a car looks bigger as it drives toward you.

My first idea was "if the box grows, beep." That beeped at everything. The
box can jump in size for one moment when someone turns, lifts an arm, or the
picture flickers. So now it looks at the last second and a half, and the
growing has to be steady, like walking. One big jump in the middle of nothing
does not count. It also has to keep being true three checks in a row before
it beeps. Walking across the hallway keeps the box about the same size, so it
stays quiet.

The other problem fooled me for a while. My Mac has two cameras: the one
built into the laptop, and the one I plugged in for the hallway. The Mac
listed them in one order, and the camera code quietly counted them in the
opposite order. So I was really watching the laptop camera, which was pointed
at my face. Every time I leaned toward the screen, my face got bigger and it
beeped, so it looked like it was working perfectly. Now it picks the hallway
camera by its name instead of its number, and I learned to grab one picture
and actually look at it before trusting any test.
