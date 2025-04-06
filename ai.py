from chess_utils import is_valid_move, get_piece_color, would_be_in_check, make_move, is_in_check

class ChessAI:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        # Simple material values
        self.piece_values = {
            'p': -100, 'P': 100,    # Pawns
            'n': -300, 'N': 300,    # Knights
            'b': -300, 'B': 300,    # Bishops
            'r': -500, 'R': 500,    # Rooks
            'q': -900, 'Q': 900,    # Queens
            'k': -2000, 'K': 2000   # Kings
        }
        self.nodes_evaluated = 0
        self.show_thinking = True

    def evaluate_board(self, board):
        """Add castling consideration to evaluation"""
        score = 0
        
        # Material evaluation
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != '.':
                    # Material value
                    score += self.piece_values.get(piece, 0)
                    
                    # Center control bonus
                    if piece.lower() in ['p', 'n'] and 2 <= i <= 5 and 2 <= j <= 5:
                        if piece.isupper():
                            score += 10
                        else:
                            score -= 10
                            
                    # Castling opportunity bonus
                    if piece == 'K' and i == 7 and j == 4:  # White king in starting position
                        if board[7][7] == 'R':  # Kingside rook present
                            score += 30
                        if board[7][0] == 'R':  # Queenside rook present
                            score += 20
                    elif piece == 'k' and i == 0 and j == 4:  # Black king in starting position
                        if board[0][7] == 'r':  # Kingside rook present
                            score -= 30
                        if board[0][0] == 'r':  # Queenside rook present
                            score -= 20
        
        return score

    def get_all_valid_moves(self, board, color):
        """Gets all valid moves for a given color"""
        moves = []
        for i in range(8):
            for j in range(8):
                if board[i][j] != '.' and get_piece_color(board, (i, j)) == color:
                    for x in range(8):
                        for y in range(8):
                            if is_valid_move(board, (i, j), (x, y), board[i][j]):
                                # Check if move is legal (doesn't put/leave own king in check)
                                if not would_be_in_check(board, (i, j), (x, y), color):
                                    # Don't capture own pieces
                                    if board[x][y] == '.' or get_piece_color(board, (x, y)) != color:
                                        moves.append(((i, j), (x, y)))
        return moves

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """Minimax algorithm with node counting"""
        self.nodes_evaluated += 1
        if depth == 0:
            return self.evaluate_board(board)

        color = 1 if maximizing_player else -1
        moves = self.get_all_valid_moves(board, color)
        
        if not moves:
            if would_be_in_check(board, None, None, color):
                return -9999 if maximizing_player else 9999  # Checkmate
            return 0  # Stalemate

        if maximizing_player:
            value = float('-inf')
            for start, end in moves:
                temp_board = make_move(board, start, end)
                value = max(value, self.minimax(temp_board, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = float('inf')
            for start, end in moves:
                temp_board = make_move(board, start, end)
                value = min(value, self.minimax(temp_board, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def get_best_move(self, board, color):
        """Gets the best move for the AI with clear thinking process output"""
        self.nodes_evaluated = 0
        moves = self.get_all_valid_moves(board, color)
        
        if not moves:
            if is_in_check(board, color):
                print("\nCheckmate! Game Over.")
            else:
                print("\nStalemate! Game Over.")
            return None

        best_move = None
        if color == 1:  # White (maximizing)
            best_value = float('-inf')
            print("\nAI Thinking Process (White):")
            print("Higher scores are better for White")
        else:  # Black (minimizing)
            best_value = float('inf')
            print("\nAI Thinking Process (Black):")
            print("Lower scores are better for Black")

        for start, end in moves:
            temp_board = make_move(board, start, end)
            value = self.minimax(temp_board, self.difficulty - 1, float('-inf'), float('inf'), color != 1)
            move_str = f"{chr(start[1] + ord('a'))}{8-start[0]} → {chr(end[1] + ord('a'))}{8-end[0]}"
            
            # Show evaluation with clear indication
            advantage = "White" if value > 0 else "Black"
            print(f"Move {move_str}: score = {value} (favors {advantage})")
            
            if (color == 1 and value > best_value) or (color == -1 and value < best_value):
                best_value = value
                best_move = (start, end)
                print(f"✓ New best move! {move_str}")

        print(f"\nFinal decision:")
        print(f"→ Move: {chr(best_move[0][1] + ord('a'))}{8-best_move[0][0]} to {chr(best_move[1][1] + ord('a'))}{8-best_move[1][0]}")
        print(f"→ Final score: {best_value}")
        print(f"→ Positions evaluated: {self.nodes_evaluated}\n")
        
        return best_move