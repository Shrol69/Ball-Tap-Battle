# Ball Tap Battle

Ball Tap Battle is a simple two-player game built with Python using the `tkinter` library. Players control sticks to hit a ball and score goals. The game ends when one player reaches 5 points.

## Features

- **Two-Player Gameplay**: Player 1 uses `W` and `S` keys, Player 2 uses `Up` and `Down` keys.
- **Score Tracking**: Scores are displayed on the screen, and the game ends when a player reaches 5 points.
- **Interactive Menu**: Players can enter their names and start the game from a menu.

## Installation

To run this game, you need to have Python installed on your machine. The game uses the built-in `tkinter` library, which is included with Python.

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Shrol69/ball-tap-battle.git
    ```

2. **Navigate to the Directory**:
    ```bash
    cd ball-tap-battle
    ```

3. **Run the Game**:
    ```bash
    python game.py
    ```

## How to Play

1. **Start the Game**: Enter player names and click "Start Game".
2. **Control the Players**:
   - Player 1: Use `W` to move up and `S` to move down.
   - Player 2: Use `Up` arrow to move up and `Down` arrow to move down.
3. **Score Goals**: Hit the ball into the opponent's goal to score points.
4. **Winning the Game**: The first player to reach 5 points wins the game.

## Game Mechanics

- **Ball Movement**: The ball bounces off the walls and players. It resets to the center when a goal is scored.
- **Player Movement**: Players move up and down within their restricted area.
- **Goals**: Goals are located at both ends of the field.

## Acknowledgements

- The game uses the `tkinter` library for creating the graphical user interface.
