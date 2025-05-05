![tic-tac-toe](https://github.com/user-attachments/assets/694fe474-b14e-4b9d-a225-41bbe6e3e160)


# Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game built in Python.

## Description

This project is a terminal-based Tic Tac Toe game where two players can compete against each other. The game provides a clean interface with a numerical keypad layout (1-9) for easy position selection.

## Features

- Interactive command-line interface
- Clear board display after each move
- Player marker selection (X or O)
- Random selection of first player
- Input validation for player choices
- Win detection for all possible winning combinations
- Draw detection when the board is full
- Option to replay after game completion

## File Structure

- `tictactoe.py` - Contains all game functions and logic
- `main.py` - The main script to run the game

## How to Play

1. Run `main.py` to start the game
2. Choose your marker (X or O)
3. The game will randomly select which player goes first
4. On your turn, enter a number from 1-9 corresponding to the position:

```
7 | 8 | 9
--|---|--
4 | 5 | 6
--|---|--
1 | 2 | 3
```

5. The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins
6. If all spaces are filled with no winner, the game ends in a draw
7. After the game ends, you can choose to play again

## Game Controls

- Position selection: Numbers 1-9 (corresponding to the keypad layout)
- Play again: 'y' (yes) or 'n' (no)
- Marker selection: 'X' or 'O'

## Requirements

- Python 3.x
- Standard libraries: os, random

## Installation

1. Clone the repository or download the files
2. Navigate to the project directory
3. Run the game with Python:

```bash
python main.py
```

## Code Structure

### tictactoe.py

Contains all the core game functions:

- `display_board()`: Displays the current state of the game board
- `player_input()`: Handles player marker selection (X or O)
- `place_marker()`: Updates the board with a player's move
- `win_check()`: Checks if a player has won
- `choose_first()`: Randomly determines which player goes first
- `space_check()`: Verifies if a space on the board is available
- `full_board_check()`: Checks if the board is full (draw condition)
- `player_choice()`: Processes player's position selection
- `replay()`: Handles the game replay option

### main.py

Contains the main game loop and orchestrates the game flow by utilizing the functions from tictactoe.py.

## Future Improvements

Potential enhancements for future versions:

- Add a single-player mode with AI opponent
- Implement difficulty levels for AI
- Add a graphical user interface
- Keep track of scores across multiple games
- Add customizable board sizes

## License

This project is open source and available for anyone to use and modify.

## Author

I created this as a Python learning project.
