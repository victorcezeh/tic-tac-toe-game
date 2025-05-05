# i am going to do this shit again and get the code right this time around!
# might do it multiple times but will get this shit right!

import random
import os


# Step 1: Create a function to print the Tic Tac Toe board.
#         Represent the board as a list where indices 1-9 correspond to a number pad.
#         This will display a 3x3 board.

def display_board(board):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("--|---|--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--|---|--")
    print(board[1] + " | " + board[2] + " | " + board[3])
    

# Step 2: Create a function to take player input and assign their marker ('X' or 'O').
#         Use a while loop to ensure valid input.

def player_input():
    marker = " "
    while marker not in ["X", "O"]:
        marker = input("Pick between X and O: ").upper()
        
    player1_marker = marker
    if player1_marker == "X":
        player2_marker = "O"
        
    else: player2_marker = "X"
    
    return (player1_marker, player2_marker)


# Step 3: Create a function to update the board with a player's marker.
#         This function should take the board list, the player's marker, and the position (1-9).

def place_marker(board, marker, position):
    board[position] = marker
    

# Step 4: Create a function to check if a player has won.
#         This function should take the board and check if there is a winning combination.

def win_check(board, mark):
    
    return((board[7] == board[8] == board[9] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[1] == board[2] == board[3] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[6] == board[9] == mark) or
           (board[7] == board[5] == board[3] == mark) or
           (board[1] == board[5] == board[9] == mark))
    

# Step 5: Create a function that randomly selects which player goes first.
#         Use the random module (random.randint()) to determine this.

def choose_first():
    flip = (random.randint(0,1))
    
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


# Step 6: Create a function that checks if a space on the board is free.
#         Return True if the space is available, otherwise return False.

def space_check(board, position):
    
    return board[position] == " "


# Step 7: Create a function that checks if the board is full.
#         Return True if there are no available spaces, otherwise return False.

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Step 8: Create a function to ask the player for their next position (1-9).
#         Use the function from step 6 to check if the position is free before returning it.

def player_choice(board):
    
    position = 0
    
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Kindly pick between number 1-9: "))
        
    return position
        

# Step 9: Create a function to ask the player if they want to play again.
#         Return True if they do, otherwise return False.

def replay():
    
    play_again = "WRONG"
    
    while play_again not in ["y", "n"]:
        play_again = input("Do you want to play again? y or n? ").lower()
        
    if play_again == "y":
            return True
    
    return False
        

# Step 10: Use while loops and the functions above to run the game.
# Manage turns, check for wins, and handle replays.
# Run game in main.py