
# Asteroids

A classic Asteroids arcade game built with Python and Pygame as a guided project of [boot.dev]("boot.dev").

## Overview

Destroy asteroids while avoiding collisions. Shoot incoming asteroids to split them into smaller pieces. Survive as long as possible!

## Gameplay

- **Move**: `W` / `↑` (forward), `S` / `↓` (backward)
- **Rotate**: `A` / `←` (left), `D` / `→` (right)
- **Shoot**: `SPACE`

## Screenshot
![screenshot](./image.png)

## Features

- Player-controlled triangle ship
- Randomly spawning asteroids from screen edges
- Asteroid splitting mechanics
- Collision detection
- Shot cooldown system
- Event logging

## Installation

```bash
pip install pygame
python main.py
```

## Project Structure

- `main.py` - Game loop and initialization
- `player.py` - Player ship class
- `asteroid.py` - Asteroid class with split mechanics
- `asteroidfield.py` - Asteroid spawning system
- `shot.py` - Projectile class
- `circleshape.py` - Base collision class
- `constants.py` - Game configuration values
- `logger.py` - Event and state logging

## Requirements

- Python 3.8+
- Pygame
