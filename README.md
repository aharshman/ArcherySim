# Archery Clicker Game

## Overview

This is a simple graphical archery game built using Python and the `graphics.py` library. The game allows multiple players to take turns shooting arrows at a target. Each player gets three shots, and their scores are calculated based on the distance of their shots from the bullseye. The player with the highest score wins!

## Features

- **Multiplayer Support**: The game allows two or more players to compete.
- **Visual Gameplay**: Players click on the window to shoot arrows, and their results are visually represented.
- **Scoring System**: Points are awarded based on how close the shot is to the bullseye.
- **Winner Announcement**: After all players have taken their turns, the player with the highest score is announced as the winner.

## Requirements

- Python 3.x
- `graphics.py` library (available [here](http://mcsp.wartburg.edu/zelle/python/graphics.py))
- `time` and `math` standard Python libraries

## How to Play

1. Clone or download this repository.
2. Install the required `graphics.py` library if you haven't already.
3. Run the script using Python:

    ```sh
    python archery_clicker.py
    ```

4. Upon starting, players will be asked how many people are playing.
5. Each player takes turns shooting three arrows by clicking on the window.
6. Points are awarded based on the distance from the target.
7. After all players have taken their turns, the player with the highest score is announced as the winner.

## Game Instructions

1. **Number of Players**: After launching the game, you'll be prompted to enter the number of players.
2. **Shooting Arrows**: Click inside the target to shoot your arrows. Each player will have three shots.
3. **Scoring**: The target is divided into five rings:
    - **Center (25 units radius)**: 50 points
    - **Next ring (50 units radius)**: 40 points
    - **Next ring (75 units radius)**: 30 points
    - **Next ring (100 units radius)**: 20 points
    - **Outer ring (125 units radius)**: 10 points
4. **Winner Announcement**: Once all players have taken their turns, the winner is announced.

## Code Structure

- `main()`: Main function that initializes the game.
- **Game Flow**:
  - Draws the game window and initializes graphical elements.
  - Asks for the number of players.
  - Players take turns shooting arrows, and their scores are calculated.
  - Winner is announced based on the total score.

## Future Improvements

- **Error Handling**: Handle invalid inputs more gracefully.
- **Enhanced Graphics**: Improve the visual elements for a more modern look.
- **Additional Features**: Add player names, more scoring options, or extra rounds.

## Notes

- The game window must be clicked to shoot an arrow.
- Make sure to follow the prompts and take turns as indicated.

## License

This project is open source and available.

---

**Author**: Alexander Harshman

