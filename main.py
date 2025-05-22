"""
Main Game Loop for Tic Tac Toe

This module contains the main game execution logic that orchestrates the
complete Tic Tac Toe gaming experience using functions from the tictactoe module.
It handles the game flow, player turns, win/draw detection, and replay functionality.

Author: V
Version: 1.0
"""

from tictactoe import (
    display_board, 
    player_input, 
    place_marker, 
    win_check, 
    choose_first, 
    space_check, 
    full_board_check, 
    player_choice, 
    replay
)


def main():
    """
    Main game function that orchestrates the complete Tic Tac Toe experience.
    
    This function manages the overall game flow including:
    - Game initialization and setup
    - Player marker assignment
    - Turn management between players
    - Win/draw condition checking
    - Game restart functionality
    
    The function runs in a continuous loop until the player chooses not to
    play again, allowing for multiple games in a single session.
    """
    # Welcome message for players
    print("Welcome to the Tic Tac Toe game!")

    # Main game loop - continues until player chooses to quit
    while True:
        # Initialize a fresh game board for each new game
        # Index 0 is unused; indices 1-9 represent board positions
        game_board = [" "] * 10
        
        # Get player marker preferences (X or O)
        player1_marker, player2_marker = player_input()
        
        # Randomly determine which player starts first
        player_turn = choose_first()
        print(f"{player_turn} will go first.")
    
        # Confirm the starting player is ready to begin
        play_game = input(f"{player_turn}, are you ready to play? Pick y or n: ").lower()
    
        # Validate the ready-to-play input
        while play_game not in ["y", "n"]:
            play_game = input("Please pick between y or n: ").lower()
    
        # Set game state based on player readiness
        if play_game == "y":
            game_on = True
        else: 
            game_on = False
    
        # Main gameplay loop - continues until win, draw, or quit
        while game_on:
            
            # Handle Player 1's turn
            if player_turn == "Player 1":
                # Display current board state
                display_board(game_board)
                
                # Get Player 1's move choice
                position = player_choice(game_board)
                
                # Place Player 1's marker on the board
                place_marker(game_board, player1_marker, position)
            
                # Check if Player 1 has won after this move
                if win_check(game_board, player1_marker):
                    display_board(game_board)
                    print("Congratulations, you have won the game.")
                    game_on = False  # End current game
                
                else:
                    # Check for draw condition (board full, no winner)
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("This is a draw!")
                        break  # Exit game loop
                
                    else:
                        # Switch to Player 2's turn
                        player_turn = "Player 2"
                    
            # Handle Player 2's turn        
            else:  # Player 2 turn
                # Display current board state
                display_board(game_board)
                
                # Get Player 2's move choice
                position = player_choice(game_board)
                
                # Place Player 2's marker on the board
                place_marker(game_board, player2_marker, position)
            
                # Check if Player 2 has won after this move
                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print("Congratulations, you have won the game.")
                    game_on = False  # End current game
                
                else:
                    # Check for draw condition (board full, no winner)
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("This is a draw!")
                        break  # Exit game loop
                
                    else: 
                        # Switch to Player 1's turn
                        player_turn = "Player 1"
                
        # After game ends, ask if players want to play again
        # If they don't want to replay, break out of main loop
        if not replay():
            break


# Entry point of the program
# This ensures main() only runs when the script is executed directly,
# not when imported as a module
if __name__ == "__main__":
    main()