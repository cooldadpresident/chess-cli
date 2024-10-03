class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "white"
    # gain coordinates and validate input
    def turn(self, player):
        while True: 
            # get the start position
            start_file = input(f"Enter the start file (A-H) for {player}: ").lower()
            if start_file not in 'abcdefgh':
                # to do add exception for value out of range 
                print("Invalid input, not a letter or the value is out of range!!")
                continue
            try:
                start_rank = int(input(f"Enter the start rank (1-8) for {player}: "))
                if start_rank > 8 or start_rank < 1:
                    print("Invalid input, not a number or the value is out for range!!")
                    continue

                
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            start_column = ord(start_file) - ord('a')
            start_row = 8 - start_rank
                    
            # get the destination position
            destination_file = input(f"Enter the destination file (A-H) for {player}: ").lower()
            if destination_file not in 'abcdefgh':
                # todo add exception value out of range
                print("Invalid input not a letter or the value is out of range")
                continue
            try:
                destination_rank = int(input(f"Enter the destination rank (1-8) for {player}: "))
                if destination_rank > 8 or destination_rank < 1:
                    print("Invalid input, not a number or value out of range!!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
            destination_column = ord(destination_file) - ord("a")
            destination_row = 8 - destination_rank
            
            # move the piece
            piece = self.board[start_row][start_column]
            
            # check if the square is not empty 
            if piece == "":
                print("Invalid move, start square is empty")
                continue
            
            if player == "white" and piece.islower():
                print("You can't move this piece it is not yours")
                continue
            if player == "black" and piece.isupper():
                print("Invalid move, it is not your piece")
                continue
            # check if the destination square contains a piece of the same player color
            destination_piece = self.board[destination_row][destination_column]
            if destination_piece != "":
                if player == "white" and destination_piece.islower():
                    print("Invalid move, you can't capture your own piece")
                    continue
                if player == "black" and destination_piece.isupper():
                    print("Invalid mode, you can't capture your own piece")
                    continue
                
            
            self.board[start_row][start_column] = ""
            self.board[destination_row][destination_column] = piece
            
            # print the updated board
            self.print_board()
            
            # switch player
            if player == "white":
                return "black"
            else:
                return "white"
        
player = "white"
game = ChessGame()
game.print_board()
while True:
    player = game.turn(player)

