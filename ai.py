from game import is_valid_move, get_piece_color, would_be_in_check

class ChessAI:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        # Piece values for board evaluation
        self.piece_values = {
            'p': -1, 'P': 1,   # Pawns
            'n': -3, 'N': 3,   # Knights
            'b': -3, 'B': 3,   # Bishops
            'r': -5, 'R': 5,   # Rooks
            'q': -9, 'Q': 9,   # Queens
            'k': -100, 'K': 100 # Kings
        }

    def evaluate_board(self, board):
        """Evaluates the current board position"""
        score = 0
        for row in board:
            for piece in row:
                if piece != '.':
                    score += self.piece_values.get(piece, 0)
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
                                if not would_be_in_check(board, (i, j), (x, y), color):
                                    moves.append(((i, j), (x, y)))
        return moves

    def minimax(self, board, depth, alpha, beta, maximizing_player, color):
        """Minimax algorithm with alpha-beta pruning"""
        if depth == 0:
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for start, end in self.get_all_valid_moves(board, color):
                # Make temporary move
                temp_board = [row[:] for row in board]
                temp_board[end[0]][end[1]] = temp_board[start[0]][start[1]]
                temp_board[start[0]][start[1]] = '.'
                
                eval = self.minimax(temp_board, depth - 1, alpha, beta, False, -color)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = float('inf')
            for start, end in self.get_all_valid_moves(board, -color):
                # Make temporary move
                temp_board = [row[:] for row in board]
                temp_board[end[0]][end[1]] = temp_board[start[0]][start[1]]
                temp_board[start[0]][start[1]] = '.'
                
                eval = self.minimax(temp_board, depth - 1, alpha, beta, True, color)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval

    def get_best_move(self, board, color):
        """Gets the best move for the AI"""
        best_move = None
        best_eval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        
        for start, end in self.get_all_valid_moves(board, color):
            temp_board = [row[:] for row in board]
            temp_board[end[0]][end[1]] = temp_board[start[0]][start[1]]
            temp_board[start[0]][start[1]] = '.'
            
            eval = self.minimax(temp_board, self.difficulty - 1, alpha, beta, False, color)
            if eval > best_eval:
                best_eval = eval
                best_move = (start, end)
                
        return best_move