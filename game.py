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

def is_valid_move(board, start, end, piece):
    """Validates if a piece can move to the target position"""
    start_row, start_col = start
    end_row, end_col = end
    
    # Calculate movement deltas
    row_diff = end_row - start_row
    col_diff = end_col - start_col
    
    piece = piece.lower()  # Convert to lowercase for checking piece type
    
    # Pawn movement
    if piece == 'p':
        # White pawns move up (negative row diff), black pawns move down (positive row diff)
        direction = -1 if board[start_row][start_col].isupper() else 1
        
        # Regular move forward
        if col_diff == 0 and row_diff == direction and board[end_row][end_col] == '.':
            return True
            
        # Initial two-square move
        if (start_row == 6 and direction == -1) or (start_row == 1 and direction == 1):
            if col_diff == 0 and row_diff == 2 * direction and board[end_row][end_col] == '.':
                # Check if path is clear
                middle_row = start_row + direction
                if board[middle_row][start_col] == '.':
                    return True
                    
        # Capture diagonally
        if abs(col_diff) == 1 and row_diff == direction:
            if board[end_row][end_col] != '.' and get_piece_color(board, end) != get_piece_color(board, start):
                return True
    
    # Rook movement
    elif piece == 'r':
        if row_diff == 0 or col_diff == 0:
            return is_path_clear(board, start, end)
    
    # Knight movement
    elif piece == 'n':
        return (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff) == 2)
    
    # Bishop movement
    elif piece == 'b':
        if abs(row_diff) == abs(col_diff):
            return is_path_clear(board, start, end)
    
    # Queen movement
    elif piece == 'q':
        if row_diff == 0 or col_diff == 0 or abs(row_diff) == abs(col_diff):
            return is_path_clear(board, start, end)
    
    # King movement
    elif piece == 'k':
        return abs(row_diff) <= 1 and abs(col_diff) <= 1
    
    return False

def is_path_clear(board, start, end):
    """Check if there are any pieces between start and end positions"""
    start_row, start_col = start
    end_row, end_col = end
    
    row_direction = 0 if start_row == end_row else (end_row - start_row) // abs(end_row - start_row)
    col_direction = 0 if start_col == end_col else (end_col - start_col) // abs(end_col - start_col)
    
    current_row = start_row + row_direction
    current_col = start_col + col_direction
    
    while (current_row, current_col) != (end_row, end_col):
        if board[current_row][current_col] != '.':
            return False
        current_row += row_direction
        current_col += col_direction
    
    # Check if destination square is empty or contains enemy piece
    if board[end_row][end_col] != '.':
        return get_piece_color(board, end) != get_piece_color(board, start)
    
    return True

def find_king(board, color):
    """Find the position of the king of given color"""
    king = 'K' if color == 1 else 'k'
    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                return (i, j)
    return None

def is_in_check(board, color):
    """Check if the king of given color is in check"""
    king_pos = find_king(board, color)
    if not king_pos:
        return False
    
    # Check if any opponent piece can capture the king
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.' and get_piece_color(board, (i, j)) == -color:
                if is_valid_move(board, (i, j), king_pos, piece):
                    return True
    return False

def would_be_in_check(board, start, end, color):
    """Check if making a move would put/leave own king in check"""
    # Make temporary move
    temp_board = [row[:] for row in board]
    temp_board[end[0]][end[1]] = temp_board[start[0]][start[1]]
    temp_board[start[0]][start[1]] = '.'
    
    return is_in_check(temp_board, color)

def main():
    
    white = 1
    black = -1
    board = initialize_board()
    player_turn = white
    
    while True:
        print_board(board, player_turn)
        
        # Show check status
        if is_in_check(board, player_turn):
            print("Check!")
            
        print(f"Player {'White' if player_turn == 1 else 'Black'}'s turn")
        
        start, end = get_player_move()
        
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
