def is_movable_piece(piece):
    # Implement logic to check if the piece is movable
    return True  # For now, assume all pieces are movable

def is_legal_move(piece, start_row, start_col, end_row, end_col):
    # Implement logic to check if the move is legal according to chess rules
    return True  # For now, assume all moves are legal

def make_move(start_row, start_col, end_row, end_col):
    piece_at_location = board[start_row][start_col]
    if not is_movable_piece(piece_at_location):
        print("Invalid move: piece is not movable")
        return

    if not is_legal_move(piece_at_location, start_row, start_col, end_row, end_col):
        print("Invalid move: move is not legal")
        return

    board[end_row][end_col] = piece_at_location
    board[start_row][start_col] = ""

    print("Move successful!")
    print_board()

def turn():
    while True:
        # Get start coordinates
        file = input("Enter letter A-H: ")
        file_lower = file.lower()
        if file_lower not in "abcdefgh":
            print("Invalid input. Please enter a letter between A and H.")
            continue
        index = input("Enter number 1-8 ")
        try:
            index = int(index)
            if index < 1 or index > 8:
                print("Invalid input. Please enter a number between 1 and 8.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        start_row = index - 1
        start_col = ord(file_lower) - ord('a')

        # Get destination coordinates
        dest_file = input("Enter destination letter A-H: ")
        dest_file_lower = dest_file.lower()
        if dest_file_lower not in "abcdefgh":
            print("Invalid input. Please enter a letter between A and H.")
            continue
        dest_index = input("Enter destination number 1-8 ")
        try:
            dest_index = int(dest_index)
            if dest_index < 1 or dest_index > 8:
                print("Invalid input. Please enter a number between 1 and 8.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        end_row = dest_index - 1
        end_col = ord(dest_file_lower) - ord('a')

        make_move(start_row, start_col, end_row, end_col)

turn()