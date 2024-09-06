# function for defining ASCII figures for chess pieces
# p = Pawn White, P = pawn black
def get_piece_symbol(piece):
    pieces = {
        "p": "p",  # Pawn (white)
        "P": "P",  # Pawn (black)
        "r": "r",  # Rook (white)
        "R": "R",  # Rook (black)oard
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



# Chess Game class for grouping all methods together and choosing the color of the player, initializing the board
class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "white"
# creates a 2D array board with 8 rows and 8 columns. Each element of the array can store the piece occupying that square on the chessboard
    def initialize_board(self):
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
        return board 
    
        # Print the chessboard with each square differentiated by color
    def print_board(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    print(f"[{get_piece_symbol(self.board[i][j])}]", end=" ")
                else:
                    print(f"{{{get_piece_symbol(self.board[i][j])}}}", end=" ")
            print()

    # gain coordinates and validate input
    def turn(self, player):
        while True: 
            # get the start position
            start_file = input(f"Enter the start file (A-H) for {player}: ").lower()
            if start_file not in 'abcdefgh':
                # to do add exception for value out of range 
                print("Invalid input, not a letter or the value is out of range!!")
                continue
            try:
                start_rank = int(input(f"Enter the start rank (1-8) for {player}: "))
                if start_rank > 8 or start_rank < 1:
                    print("Invalid input, not a number or the value is out for range!!")
                    continue

                
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            start_column = ord(start_file) - ord('a')
            start_row = 8 - start_rank
                    
            # get the destination position
            destination_file = input(f"Enter the destination file (A-H) for {player}: ").lower()
            if destination_file not in 'abcdefgh':
                # todo add exception value out of range
                print("Invalid input not a letter or the value is out of range")
                continue
            try:
                destination_rank = int(input(f"Enter the destination rank (1-8) for {player}: "))
                if destination_rank > 8 or destination_rank < 1:
                    print("Invalid input, not a number or value out of range!!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
            destination_column = ord(destination_file) - ord("a")
            destination_row = 8 - destination_rank
            
            # move the piece
            piece = self.board[start_row][start_column]
            
            # check if the square is not empty 
            if piece == "":
                print("Invalid move, start square is empty")
                continue
            
            if player == "white" and piece.islower():
                print("You can't move this piece it is not yours")
                continue
            if player == "black" and piece.isupper():
                print("Invalid move, it is not your piece")
                continue
            
            
            self.board[start_row][start_column] = ""
            self.board[destination_row][destination_column] = piece
            
            # print the updated board
            self.print_board()
            
            # switch player
            if player == "white":
                return "black"
            else:
                return "white"
        
player = "white"
game = ChessGame()
game.print_board()
while True:
    player = game.turn(player)




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
