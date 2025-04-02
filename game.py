# game.py

from board import initialize_board, print_board
from player import get_player_move, move_piece

def get_piece_color(board, position):
    """Returns 1 for white pieces, -1 for black pieces, 0 for empty squares"""
    piece = board[position[0]][position[1]]
    if piece.isupper():  # White pieces are uppercase
        return 1
    elif piece.islower():  # Black pieces are lowercase
        return -1
    return 0

def main():
    white = 1
    black = -1
    board = initialize_board()
    player_turn = white
    
    while True:
        print_board(board, player_turn)
        print(f"Player {'White' if player_turn == 1 else 'Black'}'s turn")
        
        start, end = get_player_move()
        
        # Check if player is trying to move their own piece
        piece_color = get_piece_color(board, start)
        if piece_color != player_turn:
            print("You can only move your own pieces!")
            continue
            
        if move_piece(board, start, end):
            # Switch turns between players
            if player_turn == white:
                player_turn = black
            else:
                player_turn = white

if __name__ == "__main__":
    main()
