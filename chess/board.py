class Board:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        # Initialize the board with pieces
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                if i == 1:
                    row.append(Pawn('black'))
                elif i == 6:
                    row.append(Pawn('white'))
                elif i == 0:
                    if j in [0, 7]:
                        row.append(Rook('black'))
                    elif j in [1, 6]:
                        row.append(Knight('black'))
                    elif j in [2, 5]:
                        row.append(Bishop('black'))
                    elif j == 3:
                        row.append(Queen('black'))
                    elif j == 4:
                        row.append(King('black'))
                elif i == 7:
                    if j in [0, 7]:
                        row.append(Rook('white'))
                    elif j in [1, 6]:
                        row.append(Knight('white'))
                    elif j in [2, 5]:
                        row.append(Bishop('white'))
                    elif j == 3:
                        row.append(Queen('white'))
                    elif j == 4:
                        row.append(King('white'))
                else:
                    row.append(None)
            board.append(row)
        return board