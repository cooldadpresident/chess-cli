def get_piece_color(board, position):
    """Returns 1 for white pieces, -1 for black pieces, 0 for empty squares"""
    piece = board[position[0]][position[1]]
    if piece.isupper():
        return 1
    elif piece.islower():
        return -1
    return 0

def make_move(board, start, end):
    """Make a move on the board and return the new board state"""
    temp_board = [row[:] for row in board]
    piece = temp_board[start[0]][start[1]]
    temp_board[end[0]][end[1]] = piece
    temp_board[start[0]][start[1]] = '.'
    
    # Handle promotion
    if is_promotion_move(temp_board, start, end):
        color = 1 if piece.isupper() else -1
        handle_promotion(temp_board, end, color)
    
    return temp_board

def is_valid_move(board, start, end, piece):
    """Validates if a piece can move to the target position"""
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
    
    # King movement
    elif piece == 'k':
        return abs(row_diff) <= 1 and abs(col_diff) <= 1
    
    return False

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