# game.py

from board import initialize_board, print_board
from player import get_player_move, move_piece 

def main():
    white = 1
    black = -1
    board = initialize_board()  # Set up the initial board
    player_turn = white # 1 for white, -1 for black
    
    while True:
        print_board(board, player_turn)  # Pass player_turn to print_board
        print(f"Player {'White' if player_turn == 1 else 'Black'}'s turn")  # Indicate whose turn it is
        
        start, end = get_player_move()  # Get the player's move
        
        if move_piece(board, start, end):  # Attempt to move the piece
            player_turn *= black  # Switch turns

if __name__ == "__main__":
    main()  # Start the game
