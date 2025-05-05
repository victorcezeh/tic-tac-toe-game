from tictactoe import display_board, player_input, place_marker, win_check, choose_first, space_check, full_board_check, player_choice, replay



def main():

    print("Welcome to the Tic Tac Toe game!")

    while True:
        game_board = [" "] * 10
        player1_marker, player2_marker = player_input()
        player_turn = choose_first()
        print(f"{player_turn} will go first.")
    
        play_game = input(f"{player_turn}, are you ready to play? Pick y or n:" ).lower()
    
        while play_game not in ["y","n"]:
            play_game = input("Please pick between y or n: ").lower()
    
        if play_game == "y":
                game_on = True
        
        else: 
            game_on = False
    
        while game_on:
                
            if player_turn == "Player 1":
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board, player1_marker, position)
            
                if win_check(game_board, player1_marker):
                    display_board(game_board)
                    print("Congratulations, you have won the game.")
                    game_on = False
                
                else:
                
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("This is a draw!")
                        break
                
                    else:
                        player_turn = "Player 2"
                    
                    
                
            else: #Player 2 turn
                
            
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board, player2_marker, position)
            
                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print("Congratulations, you have won the game.")
                    game_on = False
                
                else:
                
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("This is a draw!")
                        break
                
                    else: player_turn = "Player 1"
                
        if not replay():
            break
    
    

if __name__ == "__main__":
    main()