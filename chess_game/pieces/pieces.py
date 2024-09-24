#piece/pieces.py

# blueprint for creating objects for chess pieces, template that defines the properties and behaviors of an object

class Piece:
        # special method that is called when the object is created
        def __init__(self, symbol, color):
                if color not in ['white', 'black']:
                        raise ValueError('Invalid color')
                # self is a reference to that object being created
                self.symbol = symbol
                self.color = color
        # returns string representation of the object
        def __str__(self):
                return self.symbol

# subclasses of the Piece class
class Pawn(Piece):
    def __init__(self, color):
        super().__init__('P', color)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('N', color)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('B', color)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('R', color)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('Q', color)

class King(Piece):
    def __init__(self, color):
        super().__init__('K', color) 