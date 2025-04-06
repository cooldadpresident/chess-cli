# New file: game_history.py
class GameHistory:
    def __init__(self):
        self.moves = []
        self.positions = []
        
    def add_move(self, start, end, piece, captured=None):
        self.moves.append({
            'start': start,
            'end': end,
            'piece': piece,
            'captured': captured
        })