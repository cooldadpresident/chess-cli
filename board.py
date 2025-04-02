# board.py

def initialize_board():
    # Initialize a standard chess board
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
    return board

def print_board(board, player_turn):
    """Print the chess board with improved formatting"""
    # ANSI color codes
    WHITE_PIECE = "\033[97m"    # Bright white for white pieces
    BLACK_PIECE = "\033[30m"    # Black for black pieces
    WHITE_SQUARE = "\033[47m"   # White background
    BLACK_SQUARE = "\033[43m"   # Yellow background
    RESET = "\033[0m"
    
    # Unicode chess pieces
    pieces = {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
        'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
    }
    
    # Board border
    horizontal_line = "   +" + "-" * 33 + "+"
    
    # Print column labels
    print("\n     a   b   c   d   e   f   g   h")
    print(horizontal_line)
    
    # Determine row order based on player's turn
    rows = range(8) if player_turn == 1 else range(7, -1, -1)
    
    for i in rows:
        # Print row number
        print(f" {8-i} |", end=" ")
        
        for j in range(8):
            # Determine square color
            is_white_square = (i + j) % 2 == 0
            bg_color = WHITE_SQUARE if is_white_square else BLACK_SQUARE
            
            # Get piece and its color
            piece = board[i][j]
            if piece != '.':
                piece_color = WHITE_PIECE if piece.isupper() else BLACK_PIECE
                piece_symbol = pieces.get(piece, piece)
                print(f"{bg_color}{piece_color} {piece_symbol} {RESET}", end="")
            else:
                print(f"{bg_color}   {RESET}", end="")
                
        print(f" | {8-i}")
    
    print(horizontal_line)
    print("     a   b   c   d   e   f   g   h\n")

