class Piece:
    def __init__(self, symbol, color):
        self.symbol = symbol
        self.color = color

    @staticmethod
    def get_piece_symbol(piece):
        piece_symbols = {
            'P': 'Pawn',
            'R': 'Rook',
            'N': 'Knight',
            'B': 'Bishop',
            'Q': 'Queen',
            'K': 'King'
        }
        return piece_symbols.get(piece.symbol, 'Unknown')

class Pawn(Piece):
    def __init__(self, color):
        super().__init__('P', color)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('R', color)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('N', color)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('B', color)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('Q', color)

class King(Piece):
    def __init__(self, color):
        super().__init__('K', color)