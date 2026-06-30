# Kevin the Cube — 2D Alien Shooter Game

A 2D arcade-style alien shooter game built with Python and Pygame. Inspired by the classic Space Invaders format with custom gameplay mechanics and a persistent scoreboard.

## Features

- Fleet of alien enemies with progressive movement speed
- Player-controlled ship with bullet firing mechanics
- Lives system with game-over screen
- Persistent high-score tracking via SQL database
- Background music and sound effects
- Custom sprite assets

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

## Getting Started

### Prerequisites
- Python 3.x
- Pygame

```bash
pip install pygame
```

### Run the Game

```bash
git clone https://github.com/DrOneEyed/Kevin-the-cube.git
cd "Kevin-the-cube/Kevin The Cube Destroyer 2019-2020"
python Window.py
```

## Controls

| Key | Action |
|-----|--------|
| `←` / `→` | Move ship left / right |
| `Space` | Fire bullet |
| `Q` | Quit game |

## Project Structure

```
├── Window.py        # Game entry point & main loop
├── settings.py      # Game configuration constants
├── ship.py          # Player ship sprite and movement
├── alien.py         # Alien fleet logic
├── bullet.py        # Bullet physics
├── game_func.py     # Core game functions
├── game_stats.py    # Lives and scoring state
├── score.py         # Scoreboard display
├── ScoreBoard.sql   # Persistent high-score storage
├── img/             # Sprite assets
└── Music/           # Audio assets
```

## License

MIT