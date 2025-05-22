"""
Tic Tac Toe Game Implementation

A console-based Tic Tac Toe game for two players with a clean interface
and comprehensive game logic including win detection and replay functionality.

Author: V
Version: 1.0
"""

import random
import os


def display_board(board):
    """
    Display the current state of the Tic Tac Toe board.
    
    The board is represented as a list where indices 1-9 correspond to 
    positions on a number pad layout for intuitive player input.
    
    Args:
        board (list): A list of 10 elements where indices 1-9 represent 
                     board positions and index 0 is unused for clarity.
                     
    Board Layout:
        7 | 8 | 9
        --|---|--
        4 | 5 | 6
        --|---|--
        1 | 2 | 3
    """
    # Clear the console screen for a clean display
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display the board in a 3x3 grid format
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("--|---|--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--|---|--")
    print(board[1] + " | " + board[2] + " | " + board[3])


def player_input():
    """
    Get player marker choices from user input.
    
    Prompts the first player to choose between 'X' and 'O', then automatically
    assigns the remaining marker to the second player.
    
    Returns:
        tuple: A tuple containing (player1_marker, player2_marker) where each
               marker is either 'X' or 'O'.
    """
    marker = " "
    
    # Keep asking until player enters a valid marker
    while marker not in ["X", "O"]:
        marker = input("Pick between X and O: ").upper()
    
    # Assign markers to players    
    player1_marker = marker
    if player1_marker == "X":
        player2_marker = "O"
    else: 
        player2_marker = "X"
    
    return (player1_marker, player2_marker)


def place_marker(board, marker, position):
    """
    Place a player's marker on the board at the specified position.
    
    Args:
        board (list): The game board list to be modified.
        marker (str): The player's marker ('X' or 'O').
        position (int): The position on the board (1-9) where the marker
                       should be placed.
    """
    board[position] = marker


def win_check(board, mark):
    """
    Check if the specified marker has achieved a winning combination.
    
    Checks all possible winning combinations: three horizontal rows,
    three vertical columns, and two diagonal lines.
    
    Args:
        board (list): The current game board.
        mark (str): The marker to check for winning ('X' or 'O').
        
    Returns:
        bool: True if the marker has won, False otherwise.
    """
    # Check all possible winning combinations:
    # Horizontal rows, vertical columns, and diagonals
    return((board[7] == board[8] == board[9] == mark) or  # Top row
           (board[4] == board[5] == board[6] == mark) or  # Middle row
           (board[1] == board[2] == board[3] == mark) or  # Bottom row
           (board[1] == board[4] == board[7] == mark) or  # Left column
           (board[2] == board[5] == board[8] == mark) or  # Middle column
           (board[3] == board[6] == board[9] == mark) or  # Right column
           (board[7] == board[5] == board[3] == mark) or  # Diagonal (\)
           (board[1] == board[5] == board[9] == mark))    # Diagonal (/)


def choose_first():
    """
    Randomly determine which player goes first.
    
    Uses random number generation to fairly decide the starting player.
    
    Returns:
        str: Either "Player 1" or "Player 2" indicating who starts first.
    """
    flip = random.randint(0, 1)
    
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    """
    Check if a specific position on the board is available (empty).
    
    Args:
        board (list): The current game board.
        position (int): The position to check (1-9).
        
    Returns:
        bool: True if the position is empty (contains " "), False otherwise.
    """
    return board[position] == " "


def full_board_check(board):
    """
    Check if the board is completely full (no empty spaces remaining).
    
    Iterates through all valid board positions to determine if any spaces
    are still available for play.
    
    Args:
        board (list): The current game board.
        
    Returns:
        bool: True if the board is full (tie game), False if spaces remain.
    """
    # Check each position on the board
    for i in range(1, 10):
        if space_check(board, i):
            return False  # Found an empty space
    return True  # No empty spaces found


def player_choice(board):
    """
    Get a valid move choice from the current player.
    
    Prompts the player to enter a position (1-9) and validates that:
    1. The input is within the valid range (1-9)
    2. The chosen position is not already occupied
    
    Args:
        board (list): The current game board.
        
    Returns:
        int: A valid position choice (1-9) where the player wants to place
             their marker.
    """
    position = 0
    
    # Keep asking until a valid, unoccupied position is chosen
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Kindly pick between number 1-9: "))
        
    return position


def replay():
    """
    Ask the player if they want to play another game.
    
    Prompts for user input and validates the response to determine
    if a new game should be started.
    
    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    play_again = "WRONG"
    
    # Keep asking until a valid response is given
    while play_again not in ["y", "n"]:
        play_again = input("Do you want to play again? y or n? ").lower()
    
    if play_again == "y":
        return True
    
    return False


# Main game logic would be implemented in a separate main.py file
# using these functions to create the complete game experience