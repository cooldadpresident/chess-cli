# game.py

class Game:
        def __init__(self):
                self.board = self.initialize_board()
                self.current_turn = "white"
        
        def initialize_board(self):
                # initialize the board with pieces
                # i = row, j = column
                
                board = []
                for i in range(8):
                        row = []
                        for j in range(8):
                                if i == 1:
                                        row.append(Pawn("white"))
                                elif i == 6:
                                        row.append(Pawn("black"))
                                elif i == 0:
                                        if j == 0 or j == 7:
                                                row.append(Rook("white"))
                                        elif j == 1 or j == 6:
                                                row.append(Knight("white"))
                                        elif j == 2 or j == 5:
                                                row.append(Bishop("white"))
                                        elif j == 3:
                                                row.append(Queen("white"))
                                        elif j == 4:
                                                row.append(King("white"))
                                elif i == 7:
                                        if j == 0 or j == 7:
                                                row.append(Rook("black"))
                                        elif j == 1 or j == 6:
                                                row.append(Knight("black"))
                                        elif j == 2 or j == 5:
                                                row.append(Bishop("black"))
                                        elif j == 3:
                                                row.append(Queen("black"))
                                        elif j == 4:
                                                row.append(King("black"))
                                else:
                                        row.append(None)
                        # append the row to the board
                        board.append(row)
                return board
        def print_board(self):
                for i in range(8):
                        for j in range(8):
                                if (i + j) % 2 == 0:
                                        print(f"[{self.board[i][j].get_symbol()}]", end=" ")
                                else:
                                        print(f"{{{self.board[i][j].get_symbol()}}}", end=" ")
                        print()

        def turn(self, player):
                # handle player's turn
                while True:
                        try:
                                move = input("Enter your move: (e.g. e2e4): ")
                                # validate 
                                if not self.validate_move(move):
                                        raise ValueError("Invalid move")
                                # execute the move
                                self.execute_move(move)
                                # switch turns
                                self.current_turn = "black" if self.current_turn == "white" else "white"
                                break
                        except ValueError as e:
                                print("Invalid move: {e}")
        def execute_move(self, move):
                pass
        def validate_move(self, move):
                pass
