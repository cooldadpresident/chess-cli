# board.py

def initialize_board():
    # Initialize a standard chess board
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
    return board
def print_board(board, player_turn):
    # ANSI escape codes for colors
    
    
    WHITE_BG = "\033[47m"
    BLACK_BG = "\033[40m"
    RESET = "\033[0m"
    
    # Column labels (always the same)
    columns = "  a b c d e f g h"
    
    # Determine row order and labels based on player turn
    if player_turn == 1:  # White's perspective
        row_range = range(8)          # 1 to 8
        row_labels = range(8, 0, -1)  # 8 to 1
    else:  # Black's perspective
        row_range = range(7, -1, -1)  # 8 to 1
        row_labels = range(1, 9)      # 1 to 8
    
    print(columns)
    
    for i, row_label in zip(row_range, row_labels):
        row = board[i]
        
        print(row_label, end=" ")
        
        for j, piece in enumerate(row):
            # Alternate colors for squares
            if (i + j) % 2 == 0:
                print(WHITE_BG + piece + RESET, end=" ")
            else:
                print(BLACK_BG + piece + RESET, end=" ")
        
        # Print row label again at the end of the row
        print(row_label)
    
    # Print column labels again at the bottom
    print(columns)

