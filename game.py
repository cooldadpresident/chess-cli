# game.py

from board import initialize_board, print_board
from player import get_player_move, move_piece
from ai import ChessAI
from chess_utils import get_piece_color, is_valid_move, would_be_in_check, is_in_check, is_checkmate

def main():
    white = 1
    black = -1
    board = initialize_board()
    player_turn = white
    
    # Get game mode
    while True:
        mode = input("Select mode (1 for Player vs Player, 2 for Player vs AI): ").strip()
        if mode in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.")
    
    # Initialize AI if needed
    ai = None
    if mode == '2':
        while True:
            diff = input("Select AI difficulty (1-5): ").strip()
            if diff in ['1', '2', '3', '4', '5']:
                ai = ChessAI(difficulty=int(diff))
                break
            print("Invalid choice. Please enter a number between 1 and 5.")
    
    while True:
        print_board(board, player_turn)
        
        # Show check status
        if is_in_check(board, player_turn):
            print("Check!")
            if is_checkmate(board, player_turn):
                print(f"Checkmate! {'Black' if player_turn == -1 else 'White'} wins!")
                break
        
        print(f"Player {'White' if player_turn == 1 else 'Black'}'s turn")
        
        # Get move (from player or AI)
        if mode == '2' and player_turn == black:
            move = ai.get_best_move(board, player_turn)
            if move is None:
                break
            start, end = move
        else:
            try:
                start, end = get_player_move()
                # If playing as black, flip the coordinates
                if player_turn == black:
                    start = (7 - start[0], 7 - start[1])
                    end = (7 - end[0], 7 - end[1])
            except ValueError as e:
                print(str(e))
                continue
        
        # Check if player is trying to move their own piece
        piece_color = get_piece_color(board, start)
        if piece_color != player_turn:
            print("You can only move your own pieces!")
            continue
        
        piece = board[start[0]][start[1]]
        if not is_valid_move(board, start, end, piece):
            print("Invalid move for this piece!")
            continue
            
        # Check if move would put/leave own king in check
        if would_be_in_check(board, start, end, player_turn):
            print("This move would put/leave your king in check!")
            continue
            
        if move_piece(board, start, end):
            player_turn *= -1  # Switch turns between players

if __name__ == "__main__":
    main()
