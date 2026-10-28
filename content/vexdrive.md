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
- **A match version.** There is a second version for when the controller is
  plugged into a competition field switch. That way the robot only drives
  when the referee turns driver control on.

## The tricky part

The thing that is easy to get wrong is that the motors on the right side are
mounted backwards from the motors on the left. They are the same motors, just
flipped around to face the other way. So if you tell all four to spin
forward, the left wheels roll forward and the right wheels roll backward, and
the robot spins in a circle instead of driving. The fix is to tell the two
right motors that forward means the other way for them, and after that both
sticks push the robot the same direction.

Every robot is built a little differently, so I also wrote down what to
change when it drives wrong. If it spins when both sticks go forward, one
side is flipped. If it drives backwards, all four are. And if it is way too
fast or too slow, the motors have a different coloured gear inside than mine
do, and the program needs to be told which colour it is.
