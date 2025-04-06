# Chess CLI

A command-line chess game implemented in Python featuring both Player vs Player and Player vs AI modes.

## Features

- Player vs Player mode
- Player vs AI mode with 5 difficulty levels
- ASCII-based chess board with Unicode pieces
- Full chess rule implementation including:
  - All standard piece movements
  - Castling (kingside and queenside)
  - Check and checkmate detection
  - Pawn promotion
- Color-coded board display
- Algebraic notation input (e.g., 'e2 e4')

## Requirements

- Python 3.6 or higher
- Terminal with ANSI color support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chess-cli.git
cd chess-cli
```

## How to Play

1. Run the game:
```bash
python game.py
```

2. Select game mode:
   - 1: Player vs Player
   - 2: Player vs AI

3. If playing against AI, select difficulty (1-5)

4. Make moves using algebraic notation:
   - First enter the starting position (e.g., 'e2')
   - Then enter the destination position (e.g., 'e4')

## Game Controls

- Moves are input using algebraic notation (e.g., 'e2' for starting position)
- The board is displayed after each move
- The game automatically detects check, checkmate, and valid moves

## Project Structure

- `game.py`: Main game loop and game mode selection
- `board.py`: Board initialization and display functions
- `player.py`: Player move input and validation
- `chess_utils.py`: Chess rules and move validation
- `ai.py`: AI player implementation with minimax algorithm

## AI Implementation

The AI uses:
- Minimax algorithm with alpha-beta pruning
- Material-based position evaluation
- Multiple difficulty levels affecting search depth
- Basic positional evaluation (center control, castling opportunities)
