 # Chessboard ASCII Art Generator

This code generates an ASCII representation of a chessboard. It uses a 2D array to store the pieces on the board, and a function to print the ASCII representation of each piece.

## Code Explanation

### 1. Importing the necessary libraries

```python
import numpy as np
```

### 2. Defining the function to print the ASCII representation of each piece

```python
def print_piece(piece):
    if piece == "p":
        print("♙")  # Pawn (white)
    elif piece == "P":
        print("♟")  # Pawn (black)
    elif piece == "r":
        print("♖")  # Rook (white)
    elif piece == "R":
        print("♜")  # Rook (black)
    elif piece == "n":
        print("♘")  # Knight (white)
    elif piece == "N":
        print("♞")  # Knight (black)
    elif piece == "b":
        print("♗")  # Bishop (white)
    elif piece == "B":
        print("♝")  # Bishop (black)
    elif piece == "q":
        print("♕")  # Queen (white)
    elif piece == "Q":
        print("♛")  # Queen (black)
    elif piece == "k":
        print("♔")  # King (white)
    elif piece == "K":
        print("♚")  # King (black)
    else:
        print(" ")  # Empty square
```

This function takes a single character as input, which represents the piece on the board. It then prints the corresponding ASCII representation of the piece.

### 3. Creating the 2D array to store the pieces on the board

```python
board = [[None for j in range(8)] for i in range(8)]

```

This creates a 2D array with 8 rows and 8 columns. Each element of the array can store the piece occupying that square on the chessboard.

### 4. Defining the function to display the board

```python
def display_board():
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            print_piece(piece),
