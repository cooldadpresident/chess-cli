# function for defining ASCII figures for chess pieces
def get_piece_symbol(piece):
    pieces = {
        "p": "p",  # Pawn (white)
        "P": "P",  # Pawn (black)
        "r": "r",  # Rook (white)
        "R": "R",  # Rook (black)
        "n": "n",  # Knight (white)
        "N": "N",  # Knight (black)
        "b": "b",  # Bishop (white)
        "B": "B",  # Bishop (black)
        "q": "q",  # Queen (white)
        "Q": "Q",  # Queen (black)
        "k": "k",  # King (white)
        "K": "K",  # King (black)
    }
    return pieces.get(piece, " ")  # return the piece symbol or an empty string if the piece is not found

# creates a 2D array board with 8 rows and 8 columns. Each element of the array can store the piece occupying that square on the chessboard
board = []
for i in range(8):
    row = []
    for j in range(8):
        row.append("")
    board.append(row)

# Initialize the first rank with white pieces
board[0][0] = 'r'  # Rook
board[0][1] = 'n'  # Knight
board[0][2] = 'b'  # Bishop
board[0][3] = 'q'  # Queen
board[0][4] = 'k'  # King
board[0][5] = 'b'  # Bishop
board[0][6] = 'n'  # Knight
board[0][7] = 'r'  # Rook

# Initialize the second rank with white pawns
for i in range(8):
    board[1][i] = 'p'

# Initialize the seventh rank with black pawns
for i in range(8):
    board[6][i] = 'P'

# Initialize the eighth rank with black pieces
board[7][0] = 'R'  # Rook
board[7][1] = 'N'  # Knight
board[7][2] = 'B'  # Bishop
board[7][3] = 'Q'  # Queen
board[7][4] = 'K'  # King
board[7][5] = 'B'  # Bishop
board[7][6] = 'N'  # Knight
board[7][7] = 'R'  # Rook

# Print the chessboard with each square differentiated by color
def print_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                print(f"[{get_piece_symbol(board[i][j])}]", end=" ")
            else:
                print(f"{{{get_piece_symbol(board[i][j])}}}", end=" ")
        print()

# gain coordinates and validate input
def turn():
    print_board()
    while True:
        # get the start position
        start_file = input("Enter the start file (A-H): ").lower()
        start_rank = int(input("Enter the start rank (1-8): "))
        start_column = ord(start_file) - ord('a')
        start_row = 8 - start_rank

        # get the destination position
        destination_file = input("Enter the destination file (A-H): ").lower()
        destination_rank = int(input("Enter the destination rank (1-8): "))
        destination_column = ord(destination_file) - ord("a")
        destination_row = 8 - destination_rank

        # check if the move is legal
        piece = board[start_row][start_column]
        if not is_piece_movable(piece):
            print("Invalid move: piece is not movable")
            continue
        if not is_legal_move(piece, start_row, start_column, destination_row, destination_column):
            print("Invalid move: move is not legal")
            continue

        # move the piece
        board[start_row][start_column] = ""
        board[destination_row][destination_column] = piece

        # print the updated board
        print_board()

def is_piece_movable(piece):
    # implement the logic to check if the piece is movable
    # for now, assume all pieces are movable
    return True

def is_legal_move(piece, start_row, start_column, end_row, end_column):
    # implement logic to check if the move is legal according to the chess rules
    # for now, assume all moves are legal
    return True

turn()