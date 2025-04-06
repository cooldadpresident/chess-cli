from chess_utils import make_move

def get_player_move():
    """Get and validate player move input"""
    try:
        # Get start position
        start = input("Enter the starting position (e.g., 'e2'): ").strip().lower()
        if len(start) != 2:
            raise ValueError
            
        # Get end position
        end = input("Enter the destination position (e.g., 'e4'): ").strip().lower()
        if len(end) != 2:
            raise ValueError
            
        # Convert algebraic notation to array indices
        start_col = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_col = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])
        
        # Validate indices
        if not (0 <= start_row <= 7 and 0 <= start_col <= 7 and 
                0 <= end_row <= 7 and 0 <= end_col <= 7):
            raise ValueError
            
        return (start_row, start_col), (end_row, end_col)
        
    except (ValueError, IndexError):
        raise ValueError("Invalid move format! Use e.g., 'e2'")

def move_piece(board, start, end):
    """Execute a move on the actual game board"""
    new_board = make_move(board, start, end)
    for i in range(8):
        for j in range(8):
            board[i][j] = new_board[i][j]
    return True

