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
    LIGHT_SQUARE = "\033[105m"  # Light purple background
    DARK_SQUARE = "\033[45m"    # Dark purple background
    RESET = "\033[0m"
    
    # Unicode chess pieces
    pieces = {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
        'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
    }
    
    # Board border
    horizontal_line = "   +" + "-" * 33 + "+"
    
    print("\n     a   b   c   d   e   f   g   h")
    print(horizontal_line)
    
    for i in range(8):
        print(f" {8-i} |", end=" ")
        
        for j in range(8):
            is_light_square = (i + j) % 2 == 0
            bg_color = LIGHT_SQUARE if is_light_square else DARK_SQUARE
            
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

