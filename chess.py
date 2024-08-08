# function for defining ASCII figures for chess pieces
# p = Pawn White, P = pawn black

def print_piece(piece):
    if piece == "p":
        return "♙"  # Pawn (white)
    elif piece == "P":
        return "♟"  # Pawn (black)
    elif piece == "r":
        return "♖"  # Rook (white)
    elif piece == "R":
        return "♜"  # Rook (black)
    elif piece == "n":
        return "♘"  # Knight (white)
    elif piece == "N":
        return "♞"  # Knight (black)
    elif piece == "b":
        return "♗"  # Bishop (white)
    elif piece == "B":
        return "♝"  # Bishop (black)   
    elif piece == "q":
        return "♕"  # Queen (white)
    elif piece == "Q":
        return "♛"  # Queen (black)
    elif piece == "k":
        return "♔"  # King (white)
    elif piece == "K":
        return "♚"  # King (black)
    else:
        return " "  # Empty square

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
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(f"[{print_piece(board[i][j])}]", end=" ")
        else:
            print(f"{{{print_piece(board[i][j])}}}", end=" ")
    print()
    
def turn():
    file = input("Enter letter A-H")
    file_lower = file.lower()
    index = input("Enter number 1-8")
    index_lower = index.lower()




# chess board with its corresponding notation
'''
  a  b  c  d  e  f  g  h
8  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .
'''