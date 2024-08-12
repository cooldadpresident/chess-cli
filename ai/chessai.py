def get_piece_symbol(piece):
    pieces = {
        "p": "♙",  # Pawn (white)
        "P": "♟",  # Pawn (black)
        "r": "♖",  # Rook (white)
        "R": "♜",  # Rook (black)
        "n": "♘",  # Knight (white)
        "N": "♞",  # Knight (black)
        "b": "♗",  # Bishop (white)
        "B": "♝",  # Bishop (black)
        "q": "♕",  # Queen (white)
        "Q": "♛",  # Queen (black)
        "k": "♔",  # King (white)
        "K": "♚",  # King (black)
    }
    return pieces.get(piece, " ")  # return the piece symbol or an empty string if the piece is not found

# Initialize the chessboard
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def print_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                print(f"[{get_piece_symbol(board[i][j])}]", end=" ")
            else:
                print(f"{{{get_piece_symbol(board[i][j])}}}", end=" ")
        print()

def turn():
    print_board()
    while True:
        # Get the start position
        start_file = input("Enter the start file (A-H): ").lower()
        start_rank = int(input("Enter the start rank (1-8): "))
        start_col = ord(start_file) - ord('a')
        start_row = 8 - start_rank  # Convert rank to row index

        # Get the destination position
        dest_file = input("Enter the destination file (A-H): ").lower()
        dest_rank = int(input("Enter the destination rank (1-8): "))
        dest_col = ord(dest_file) - ord('a')
        dest_row = 8 - dest_rank  # Convert rank to row index

        # Move the piece
        piece = board[start_row][start_col]
        board[start_row][start_col] = ""
        board[dest_row][dest_col] = piece

        # Print the updated board
        print_board()

        # Add logic for breaking the loop or continue to the next turn
        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break

turn()
