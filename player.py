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
    start_row, start_col = start
    end_row, end_col = end
    
    # Basic move validation (you can expand this with actual chess rules)
    if board[start_row][start_col] == " ":
        print("No piece at the starting position.")
        return False
    if board[end_row][end_col] != " ":
        print("Destination position is not empty.")
        return False

    # Check if the player is moving their own piece
    '''
    to do!
    if board[start_row][start_col].color == board[end_row][end_col].color:
        print("You cannot move onto your own piece!")
        return False

 
    '''
       # Move the piece
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "
    return True

