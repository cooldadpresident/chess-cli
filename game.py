# game.py

from board import initialize_board, print_board
from player import get_player_move, move_piece

class GameState:
    def __init__(self):
        self.move_history = []
        self.halfmove_clock = 0  # For fifty-move rule
        self.positions = {}  # For threefold repetition
        
    def add_move(self, board, start, end, piece):
        # Convert to algebraic notation
        start_square = chr(start[1] + ord('a')) + str(8 - start[0])
        end_square = chr(end[1] + ord('a')) + str(8 - end[0])
        move = f"{piece}{start_square}-{end_square}"
        self.move_history.append(move)
        
        # Update halfmove clock
        if piece.lower() == 'p' or board[end[0]][end[1]] != '.':
            self.halfmove_clock = 0
        else:
            self.halfmove_clock += 1
            
        # Store position for threefold repetition
        position = str(board)
        self.positions[position] = self.positions.get(position, 0) + 1

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

def is_checkmate(board, color):
    """Check if the given color is in checkmate"""
    if not is_in_check(board, color):
        return False
        
    # Try all possible moves for all pieces
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.' and get_piece_color(board, (i, j)) == color:
                # Try all possible destinations
                for x in range(8):
                    for y in range(8):
                        if is_valid_move(board, (i, j), (x, y), piece):
                            # If any move prevents check, it's not checkmate
                            if not would_be_in_check(board, (i, j), (x, y), color):
                                return False
    return True

def is_stalemate(board, color):
    """Check if the given color is in stalemate"""
    if is_in_check(board, color):
        return False
        
    # Try all possible moves for all pieces
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.' and get_piece_color(board, (i, j)) == color:
                # Try all possible destinations
                for x in range(8):
                    for y in range(8):
                        if is_valid_move(board, (i, j), (x, y), piece):
                            # If any move is valid and doesn't put king in check, it's not stalemate
                            if not would_be_in_check(board, (i, j), (x, y), color):
                                return False
    return True

def can_castle(board, start, end, piece):
    """Check if castling is legal"""
    start_row, start_col = start
    end_row, end_col = end
    
    # King must not have moved
    if piece.lower() != 'k' or start_row != (7 if piece.isupper() else 0):
        return False
        
    # Must be horizontal movement of 2 squares
    if start_row != end_row or abs(end_col - start_col) != 2:
        return False
        
    # Determine rook position
    rook_col = 7 if end_col > start_col else 0
    rook = 'R' if piece.isupper() else 'r'
    
    # Check if rook is in position
    if board[start_row][rook_col] != rook:
        return False
        
    # Check if path is clear
    direction = 1 if end_col > start_col else -1
    for col in range(start_col + direction, rook_col, direction):
        if board[start_row][col] != '.':
            return False
            
    # Check if king passes through check
    temp_col = start_col
    while temp_col != end_col:
        if would_be_in_check(board, (start_row, temp_col), 
                           (start_row, temp_col + direction), 
                           get_piece_color(board, start)):
            return False
        temp_col += direction
        
    return True

def handle_pawn_promotion(board, end, color):
    """Handle pawn promotion"""
    end_row, end_col = end
    if end_row in (0, 7):  # Pawn reached opposite end
        while True:
            choice = input("Promote pawn to (Q/R/B/N): ").upper()
            if choice in ['Q', 'R', 'B', 'N']:
                board[end_row][end_col] = choice if color == 1 else choice.lower()
                break
            print("Invalid choice. Please choose Q, R, B, or N.")

def is_insufficient_material(board):
    """Check for insufficient material for checkmate"""
    pieces = {'k': 0, 'K': 0, 'b': 0, 'B': 0, 'n': 0, 'N': 0, 
              'p': 0, 'P': 0, 'r': 0, 'R': 0, 'q': 0, 'Q': 0}
    
    for row in board:
        for piece in row:
            if piece != '.':
                pieces[piece] += 1
                
    # King vs King
    if sum(pieces.values()) == 2:
        return True
    # King and Bishop/Knight vs King
    if sum(pieces.values()) == 3 and (pieces['b'] + pieces['B'] + 
                                     pieces['n'] + pieces['N'] == 1):
        return True
    return False

def main():
    
    white = 1
    black = -1
    board = initialize_board()
    player_turn = white
    game_state = GameState()
    
    while True:
        print_board(board, player_turn)
        
        # Check for checkmate
        if is_checkmate(board, player_turn):
            print(f"Checkmate! {'Black' if player_turn == 1 else 'White'} wins!")
            break
            
        # Check for stalemate
        if is_stalemate(board, player_turn):
            print("Stalemate! The game is a draw.")
            break
        
        # Show check status
        if is_in_check(board, player_turn):
            print("Check!")
            
        # Check for draws
        if game_state.halfmove_clock >= 50:
            print("Draw by fifty-move rule!")
            break
            
        if max(game_state.positions.values()) >= 3:
            print("Draw by threefold repetition!")
            break
            
        if is_insufficient_material(board):
            print("Draw by insufficient material!")
            break
            
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
            game_state.add_move(board, start, end, piece)
            player_turn *= -1  # Switch turns between players

if __name__ == "__main__":
    main()
