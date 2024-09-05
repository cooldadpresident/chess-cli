# constants
BOARD_SIZE = 8
RANKS = list(range(1, BOARD_SIZE + 1))
FILES = 'abcdefgh'

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.player = "white"

    def initialize_board(self):
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

        return board

    def print_board(self):
        # Print the chessboard with each square differentiated by color
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    print(f"[{self.get_piece_symbol(self.board[i][j])}]", end=" ")
                else:
                    print(f"{{{self.get_piece_symbol(self.board[i][j])}}}", end=" ")
            print()

    def get_piece_symbol(self, piece):
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

    def turn(self):
        while True: