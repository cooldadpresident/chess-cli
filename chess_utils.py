def get_piece_color(board, position):
    """Returns 1 for white pieces, -1 for black pieces, 0 for empty squares"""
    piece = board[position[0]][position[1]]
    if piece.isupper():
        return 1
    elif piece.islower():
        return -1
    return 0

def make_move(board, start, end):
    """Update move execution to handle castling"""
    temp_board = [row[:] for row in board]
    piece = temp_board[start[0]][start[1]]
    
    # Handle castling
    if piece.lower() == 'k' and abs(end[1] - start[1]) == 2:
        # Move king
        temp_board[end[0]][end[1]] = piece
        temp_board[start[0]][start[1]] = '.'
        
        # Move rook
        if end[1] == 6:  # Kingside
            rook_start = (start[0], 7)
            rook_end = (start[0], 5)
        else:  # Queenside
            rook_start = (start[0], 0)
            rook_end = (start[0], 3)
            
        temp_board[rook_end[0]][rook_end[1]] = temp_board[rook_start[0]][rook_start[1]]
        temp_board[rook_start[0]][rook_start[1]] = '.'
        return temp_board
        
    # Normal move
    temp_board[end[0]][end[1]] = piece
    temp_board[start[0]][start[1]] = '.'
    return temp_board

def is_valid_move(board, start, end, piece):
    """Update move validation to include castling"""
    start_row, start_col = start
    end_row, end_col = end
    
    # Check if move is within board boundaries
    if not (0 <= end_row < 8 and 0 <= end_col < 8):
        return False
    
    # Calculate movement deltas
    row_diff = end_row - start_row
    col_diff = end_col - start_col
    
    # Cannot move to same position
    if row_diff == 0 and col_diff == 0:
        return False
        
    piece = piece.lower()  # Convert to lowercase for checking piece type
    
    # Pawn movement
    if piece == 'p':
        direction = -1 if board[start_row][start_col].isupper() else 1
        
        # Basic one square forward move
        if col_diff == 0 and row_diff == direction and board[end_row][end_col] == '.':
            return True
            
        # Initial two-square move
        if (start_row == 6 and direction == -1) or (start_row == 1 and direction == 1):
            if col_diff == 0 and row_diff == 2 * direction:
                middle_row = start_row + direction
                return board[end_row][end_col] == '.' and board[middle_row][start_col] == '.'
                
        # Capture moves
        if abs(col_diff) == 1 and row_diff == direction:
            if board[end_row][end_col] != '.' and get_piece_color(board, end) != get_piece_color(board, start):
                return True
        return False
    
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
    
    # King movement including castling
    elif piece.lower() == 'k':
        if abs(row_diff) <= 1 and abs(col_diff) <= 1:
            return True
        # Check for castling
        return can_castle(board, start, end, piece)
    
    return False

def can_castle(board, start, end, piece):
    """Check if castling is legal"""
    start_row, start_col = start
    end_row, end_col = end
    
    # Basic castling conditions
    if piece.lower() != 'k':  # Must be king
        return False
    if start_row != (7 if piece.isupper() else 0):  # Must be on back rank
        return False
    if start_col != 4:  # King must be on e1/e8
        return False
    if end_row != start_row:  # Must be horizontal move
        return False
    if abs(end_col - start_col) != 2:  # Must move two squares
        return False
        
    # Check if king or rook has moved
    if piece.isupper():  # White
        if start != (7, 4):  # King must be on e1
            return False
        if end_col == 6:  # Kingside
            rook_pos = (7, 7)
            path_cols = [5, 6]
        else:  # Queenside
            rook_pos = (7, 0)
            path_cols = [1, 2, 3]
    else:  # Black
        if start != (0, 4):  # King must be on e8
            return False
        if end_col == 6:  # Kingside
            rook_pos = (0, 7)
            path_cols = [5, 6]
        else:  # Queenside
            rook_pos = (0, 0)
            path_cols = [1, 2, 3]
    
    # Check if rook is present
    rook = 'R' if piece.isupper() else 'r'
    if board[rook_pos[0]][rook_pos[1]] != rook:
        return False
        
    # Check if path is clear
    for col in path_cols:
        if board[start_row][col] != '.':
            return False
            
    # Check if king passes through check
    color = 1 if piece.isupper() else -1
    direction = 1 if end_col > start_col else -1
    temp_col = start_col
    while temp_col != end_col:
        temp_col += direction
        if would_be_in_check(board, (start_row, start_col), (start_row, temp_col), color):
            return False
            
    return True

def is_path_clear(board, start, end):
    """Check if there are any pieces between start and end positions"""
    start_row, start_col = start
    end_row, end_col = end
    
    row_step = 0 if start_row == end_row else (end_row - start_row) // abs(end_row - start_row)
    col_step = 0 if start_col == end_col else (end_col - start_col) // abs(end_col - start_col)
    
    current_row = start_row + row_step
    current_col = start_col + col_step
    
    while (current_row, current_col) != (end_row, end_col):
        if board[current_row][current_col] != '.':
            return False
        current_row += row_step
        current_col += col_step
    
    # Check if destination square is empty or contains enemy piece
    return board[end_row][end_col] == '.' or get_piece_color(board, end) != get_piece_color(board, start)

def is_in_check(board, color):
    """Check if the king of given color is in check"""
    # Find king position
    king = 'K' if color == 1 else 'k'
    king_pos = None
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        return False

    # Check if any opponent piece can capture the king
    opponent_color = -color
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.' and get_piece_color(board, (i, j)) == opponent_color:
                if is_valid_move(board, (i, j), king_pos, piece):
                    return True
    return False

def would_be_in_check(board, start, end, color):
    """Check if making a move would put/leave own king in check"""
    temp_board = make_move(board, start, end)
    return is_in_check(temp_board, color)

def is_promotion_move(board, start, end):
    """Check if move is a pawn promotion"""
    piece = board[start[0]][start[1]]
    if piece.lower() != 'p':
        return False
    
    # White pawn reaching 8th rank or black pawn reaching 1st rank
    return (piece == 'P' and end[0] == 0) or (piece == 'p' and end[0] == 7)

def handle_promotion(board, end, color):
    """Handle pawn promotion"""
    end_row, end_col = end
    while True:
        choice = input("Promote pawn to (Q/R/B/N): ").strip().upper()
        if choice in ['Q', 'R', 'B', 'N']:
            board[end_row][end_col] = choice if color == 1 else choice.lower()
            return True
    return False

def is_checkmate(board, color):
    """Check if the given color is in checkmate"""
    # First check if king is in check
    if not is_in_check(board, color):
        return False
        
    # Try all possible moves to see if any can get out of check
    for i in range(8):
        for j in range(8):
            if board[i][j] != '.' and get_piece_color(board, (i, j)) == color:
                for x in range(8):
                    for y in range(8):
                        if is_valid_move(board, (i, j), (x, y), board[i][j]):
                            # Try the move
                            temp_board = make_move(board, (i, j), (x, y))
                            if not is_in_check(temp_board, color):
                                return False
    return True