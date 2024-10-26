class Piece:
    def __init__(self, symbol, color):
        self.symbol = symbol
        self.color = color

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