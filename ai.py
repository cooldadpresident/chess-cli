from chess_utils import is_valid_move, get_piece_color, would_be_in_check, make_move

class ChessAI:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        # Enhanced piece values
        self.piece_values = {
            'p': -100, 'P': 100,     # Pawns
            'n': -320, 'N': 320,     # Knights
            'b': -330, 'B': 330,     # Bishops
            'r': -500, 'R': 500,     # Rooks
            'q': -900, 'Q': 900,     # Queens
            'k': -20000, 'K': 20000  # Kings
        }
        
        # Center control bonus
        self.center_squares = {
            (3,3): 0.3, (3,4): 0.3, 
            (4,3): 0.3, (4,4): 0.3
        }
        
        # Development bonus for minor pieces
        self.development_bonus = 0.2

    def evaluate_board(self, board):
        """Enhanced board evaluation"""
        score = 0
        
        # Material and basic position
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != '.':
                    # Material value
                    score += self.piece_values.get(piece, 0)
                    
                    # Center control bonus
                    if (i, j) in self.center_squares:
                        if piece.isupper():  # White pieces
                            score += self.center_squares[(i, j)]
                        else:  # Black pieces
                            score -= self.center_squares[(i, j)]
                    
                    # Development bonus for minor pieces
                    if piece in ['N', 'B']:  # White pieces
                        if i != 7:  # Not on starting rank
                            score += self.development_bonus
                    elif piece in ['n', 'b']:  # Black pieces
                        if i != 0:  # Not on starting rank
                            score -= self.development_bonus
                    
                    # Penalty for moving king early (except castling)
                    if piece in ['K', 'k'] and self.is_early_game(board):
                        if piece == 'K' and i != 7:
                            score -= 0.5
                        elif piece == 'k' and i != 0:
                            score += 0.5

        return score

    def is_early_game(self, board):
        """Check if it's still early game"""
        piece_count = 0
        for row in board:
            for piece in row:
                if piece != '.':
                    piece_count += 1
        return piece_count >= 24  # More than 24 pieces still on board

    def get_all_valid_moves(self, board, color):
        """Gets all valid moves for a given color"""
        moves = []
        for i in range(8):
            for j in range(8):
                if board[i][j] != '.' and get_piece_color(board, (i, j)) == color:
                    for x in range(8):
                        for y in range(8):
                            if is_valid_move(board, (i, j), (x, y), board[i][j]):
                                if not would_be_in_check(board, (i, j), (x, y), color):
                                    moves.append(((i, j), (x, y)))
        return moves

    def minimax(self, board, depth, alpha, beta, maximizing_player, color):
        """Minimax algorithm with alpha-beta pruning"""
        if depth == 0:
            return self.evaluate_board(board)

        moves = self.get_all_valid_moves(board, color if maximizing_player else -color)
        if not moves:  # No valid moves
            if would_be_in_check(board, None, None, color):
                return -9999 if maximizing_player else 9999  # Checkmate
            return 0  # Stalemate

        if maximizing_player:
            max_eval = float('-inf')
            for start, end in moves:
                temp_board = make_move(board, start, end)
                eval = self.minimax(temp_board, depth - 1, alpha, beta, False, color)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for start, end in moves:
                temp_board = make_move(board, start, end)
                eval = self.minimax(temp_board, depth - 1, alpha, beta, True, color)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, board, color):
        """Gets the best move for the AI"""
        best_move = None
        best_eval = float('-inf') if color == 1 else float('inf')
        alpha = float('-inf')
        beta = float('inf')
        
        moves = self.get_all_valid_moves(board, color)
        if not moves:
            return None
            
        # Sort moves to improve alpha-beta pruning
        moves = self.sort_moves(board, moves)
        
        for start, end in moves:
            temp_board = make_move(board, start, end)
            eval = self.minimax(temp_board, self.difficulty - 1, alpha, beta, False if color == 1 else True, color)
            
            if color == 1 and eval > best_eval:
                best_eval = eval
                best_move = (start, end)
            elif color == -1 and eval < best_eval:
                best_eval = eval
                best_move = (start, end)
                
            alpha = max(alpha, eval) if color == 1 else alpha
            beta = min(beta, eval) if color == -1 else beta
                
        return best_move

    def sort_moves(self, board, moves):
        """Sort moves to improve alpha-beta pruning"""
        move_scores = []
        for start, end in moves:
            score = 0
            piece = board[start[0]][start[1]]
            # Prioritize captures
            if board[end[0]][end[1]] != '.':
                score += 10
            # Prioritize center control
            if (end[0], end[1]) in self.center_squares:
                score += 5
            # Prioritize development
            if piece in ['N', 'B', 'n', 'b']:
                score += 3
            move_scores.append((score, (start, end)))
        
        return [move for _, move in sorted(move_scores, reverse=True)]

    def handle_ai_promotion(self, board, end, color):
        """AI always promotes to queen"""
        end_row, end_col = end
        board[end_row][end_col] = 'Q' if color == 1 else 'q'
        return board