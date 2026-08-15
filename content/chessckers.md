title: Chessckers
kind: Game
status: Live
order: 1
tagline: A full chess army against 24 stacking checkers. Playable in a browser.
platforms: Web, desktop (Godot)
stack: Godot 4.7, C#, JavaScript
links: Play in your browser | https://z1order.github.io/chessckers/
---

An implementation of **Chessckers**, the asymmetric board game where a full
chess army fights 24 stacking checkers. The game is designed, written and
illustrated by M. Edden Ishaaya and engineered by Nikita Ulianov — this project
is an implementation of the published ruleset, not the game itself.

## What it does

- **Play in a browser**, no install, no plugin, one self-contained page.
- **A solo opponent** in the web build, searching over the same rules engine.
- **A desktop build** in Godot for two players at one screen.

## Worth knowing

The rules engine is plain C# with no Godot dependency, so it can be exercised on
its own without launching a game engine. That constraint is what makes the whole
thing testable.

The web version is a second, independent port rather than an export of the Godot
project. The engine, the opponent and the interface are separate files stitched
into one self-contained page by a build script, with console test suites for
both the engine and the opponent. Both suites run headlessly on macOS through
`osascript`, so there is no Node install anywhere in the loop. The deploy
workflow rebuilds the page and runs the engine suite before publishing, which
means a broken rules change cannot reach the live site.
