# function for defining ASCII figures for chess pieces
# p = Pawn White, P = pawn black
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
    
# define a dictionary to represent the board
'''board = {}
for file in {}'''

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
        
        # move the piece
        piece = board[start_row][start_column]
        board[start_row][start_column] = ""
        board[destination_row][destination_column] = piece
        
        # print the updated board
        
        print_board()
        
        
        
        
        
        
        
"""
def turn():
    
    while True:
        # get piece and destination square
        piece_input = input("Enter piece (Pawn, Knight, Bishop, Rook, Queen, King): ")
        piece_lower = piece_input.lower()
        if piece_lower not in ["pawn", "knight", "bishop", "rook", "queen", "king"]:
            print("Invalid input. Please enter a valid piece.")
            continue
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
        
        # convert file letter to column index using ord which is a built in function that returns the Unicode code point for a give character which is 97 for a 
        column_index  = ord(file_lower) - ord('a')
        print(column_index)
        
        # convert index number to row index
        row_index = index - 1
        print(row_index)
        
        # use the validated input
        print(f"File: {file_lower.capitalize()}, Index: {index}")
        
        # identify the piece at the selected location
        
        print(piece_lower)
        board[column_index][row_index] = 'P'
        
        """
                
'''
def is_piece_movable(piece_at_location):
    # implement the logic to check if the peace is movable
    return True # for now assume all pieces are movable
def is_legal_move(piece, start_row, start_column, end_row, end_column):
    # implement logic to check if the move is legal according to the chess rules
    return True # for now assume all moves are legal
'''



        

turn()



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