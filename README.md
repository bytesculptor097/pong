# Pong Game in Python

A classic **Pong** game built with Python, simulating the iconic table tennis arcade experience. Control paddles, compete against a friend or AI, and try to score points before your opponent does. This project is a fun way to practice Python skills and get hands-on with simple game development.

---

## Features

- **Two-player mode**: Challenge a friend—each player controls a paddle.
- **Single-player mode**: Play against computer-controlled opposition.
- **Customizable controls and easy to modify.**
- **Visual score tracking** and game-over display.
- Clean and readable, well-documented Python code.

---

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

---

## Installation

1. **Clone or Download** the repository:
```
git clone https://github.com/bytesculptor097/pong
cd pong
```

2. **Ensure Python 3 is installed** on your system.
3. **Install dependencies**:
```
pip install pygame
```

---

## How to Play

- **Objective:** Use your paddle to bounce the ball past your opponent. Score points each time your opponent misses the ball.
- **Win Condition:** Reach the set score limit 5 before your opponent.
- **Controls:**
- *Right Paddle:* `W` (up), `S` (down)
- *Left Paddle:* `Up Arrow` (up), `Down Arrow` (down)
- The ball bounces off paddles and top/bottom walls. Missing returns a point to the opposing side.

---

## Usage

To run the game, execute:
```
python pong.py
```


Enjoy the game window that appears! For two players, use the assigned keys to control your paddle. Score is displayed at the top.

---

## File Structure

- `pong.py` – Main game file (all logic, drawing, and event handling)
- `assets` - All the pictures, sounds etc.

---

## Requirements

- **Python 3**
- **pygame** 
- Cross-platform (runs on Windows, macOS, and Linux)


---

## License

This project is released under the [MIT License](LICENSE).

---




