from chess_utils import make_move

def get_player_move():
    try:
        start = input("Enter the starting position (e.g., 'e2'): ").strip().lower()
        end = input("Enter the destination position (e.g., 'e4'): ").strip().lower()
        
        # Convert positions to board indices
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        
        return (start_row, start_col), (end_row, end_col)
    except (ValueError, IndexError):
        print("Invalid input. Please enter positions in the format 'e2'.")
        return get_player_move()

def move_piece(board, start, end):
    """Execute a move on the actual game board"""
    new_board = make_move(board, start, end)
    for i in range(8):
        for j in range(8):
            board[i][j] = new_board[i][j]
    return True

