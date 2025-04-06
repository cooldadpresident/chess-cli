# Chess CLI - Technical Documentation

## Code Architecture Overview

### Board Representation
- The chess board is represented as an 8x8 2D list in `board.py`
- Pieces are represented as single characters:
  - Uppercase letters for white pieces (K, Q, R, B, N, P)
  - Lowercase letters for black pieces (k, q, r, b, n, p)
  - Dots (.) for empty squares

### Core Game Logic (`chess_utils.py`)

#### Move Validation System
1. `is_valid_move(board, start, end, piece)`:
   - Validates moves based on piece type
   - Handles special cases like castling and pawn promotion
   - Returns boolean indicating move validity

2. `make_move(board, start, end)`:
   - Creates a new board state after move execution
   - Special handling for castling (rook movement)
   - Returns the new board state

3. `can_castle(board, start, end, piece)`:
   - Validates castling conditions:
     - King and rook haven't moved
     - Path between king and rook is clear
     - King doesn't move through check

#### Check Detection
1. `is_in_check(board, color)`:
   - Locates king position
   - Checks if any opponent piece can capture king
   - Used for both immediate check detection and checkmate validation

2. `would_be_in_check(board, start, end, color)`:
   - Simulates move on temporary board
   - Checks if resulting position puts own king in check
   - Prevents illegal moves that expose king

### AI Implementation (`ai.py`)

#### Minimax Algorithm
1. Core Algorithm:
   ```python
   def minimax(board, depth, alpha, beta, maximizing_player):
       if depth == 0:
           return evaluate_board(board)
       
       moves = get_all_valid_moves(board, color)
       # ...implementation with alpha-beta pruning
   ```

2. Position Evaluation:
   - Material counting (piece values)
   - Center control bonuses
   - Castling opportunity evaluation
   - Relative piece positioning

#### Move Generation
1. `get_all_valid_moves(board, color)`:
   - Generates all legal moves for given color
   - Filters moves that would result in check
   - Returns list of (start, end) move tuples

### User Interface Components

#### Board Display (`board.py`)
- ANSI color codes for piece colors and squares
- Unicode chess symbols for pieces
- Dynamic board orientation based on player turn

#### Move Input (`player.py`)
- Algebraic notation parsing (e.g., "e2 e4")
- Coordinate conversion between algebraic and array indices
- Move validation and execution

## Key Algorithms Explained

### Checkmate Detection
```python
def is_checkmate(board, color):
    # 1. Verify king is in check
    if not is_in_check(board, color):
        return False
        
    # 2. Try all possible moves
    for each piece of color:
        for each possible move:
            if move gets out of check:
                return False
                
    # 3. No legal moves found
    return True
```

### Move Validation
1. Basic validation:
   - Check if move is within board boundaries
   - Verify piece movement pattern
   - Check for obstacles in path

2. Special cases:
   - Pawn movement (first move, capture, promotion)
   - Castling conditions
   - Check prevention

### AI Evaluation Function
```python
def evaluate_board(board):
    score = 0
    # 1. Material counting
    for each piece:
        add/subtract piece value
        
    # 2. Position evaluation
    for each piece:
        add/subtract position bonus
        
    # 3. Special considerations
    evaluate castling opportunities
    evaluate center control
    
    return score
```

## Implementation Tips

1. Move Generation Optimization:
   - Generate captures first for better alpha-beta pruning
   - Cache frequently accessed board states
   - Pre-calculate possible moves for pieces

2. Check Detection:
   - Keep track of king position instead of searching
   - Only check relevant pieces for check detection
   - Use ray-tracing for sliding pieces

3. Position Evaluation:
   - Weight material value highest
   - Consider piece mobility
   - Evaluate pawn structure
   - Factor in king safety

## Common Pitfalls

1. Move Validation:
   - Don't forget en passant rules
   - Handle pawn promotion correctly
   - Verify castling through check

2. Check Detection:
   - Remember to validate intermediate squares in castling
   - Consider all possible checking pieces
   - Verify check escape moves

3. AI Implementation:
   - Balance evaluation complexity with search depth
   - Handle edge cases in position evaluation
   - Implement proper move ordering for efficiency
