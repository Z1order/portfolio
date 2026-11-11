title: VexDrive
kind: Other
status: In development
order: 7
tagline: The driving program for a VEX V5 robot. Push the sticks and the wheels move.
platforms: VEX V5 robot
stack: C++, VEXcode V5
---

VexDrive is the program that lets a person drive a VEX V5 robot with the
controller. The robot has four motors, two on each side, and each stick on
the controller runs one side. It is the first program any robot needs,
because until it can drive, it cannot do anything else.

## What it does

- **Tank drive.** The left stick drives the left wheels and the right stick
  drives the right wheels. Push both forward to go straight. Push one forward
  and one back and the robot spins in place.
- **Four motors act like two.** The two motors on each side are grouped
  together, so the program tells the whole left side to spin instead of
  talking to each motor one at a time.
- **It checks the sticks fifty times a second.** The program reads where each
  stick is, sends that speed to the wheels, waits a tiny moment, and does it
  again forever. That is fast enough that the robot feels like it is moving
  the instant you move your thumb.
- **It works at a match.** The program is the competition kind, so when the
  robot is plugged into a field switch it only drives when the referee turns
  driver control on.
- **Autonomous moves, switched off for now.** I added two commands, `drive`
  and `turn`, so the robot can move on its own at the start of a match. You
  write something like `drive(24)` to go forward 24 inches or `turn(90)` to
  turn right 90 degrees. Driving measures how far the wheels have rolled,
  and turning uses a sensor that knows which way the robot is facing. Those
  parts are commented out right now so basic driving works first, and
  button A runs the routine for testing without a field switch.

## The tricky part

The thing that is easy to get wrong is that the motors on the right side are
mounted backwards from the motors on the left. They are the same motors, just
flipped around to face the other way. So if you tell all four to spin
forward, the left wheels roll forward and the right wheels roll backward, and
the robot spins in a circle instead of driving. The fix is to tell the two
right motors that forward means the other way for them, and after that both
sticks push the robot the same direction.

The other hard part was getting the robot to stop in the right place on its
own. If you just tell it to go full speed until it has gone 24 inches, it
slides past the mark. So the autonomous code keeps asking one question: how
far am I from where I want to be? Far away, it gives lots of power. Close,
it gives a little. It also looks at how fast that gap is shrinking and
pushes back, like a brake, so it does not fly past. And if it stops just
short and sits there, a tiny extra nudge builds up until it finishes. That
is called PID, and it is three numbers you tune one at a time. I wrote a
table of what to change when the robot stops short, shoots past, or wiggles
back and forth at the end.

Every robot is built a little differently, so I also wrote down what to
change when it drives wrong. If it spins when both sticks go forward, one
side is flipped. If it drives backwards, all four are. And if it is way too
fast or too slow, the motors have a different coloured gear inside than mine
do, and the program needs to be told which colour it is.
