from game import ChessGame

def main():
    game = ChessGame()
    game.print_board()
    while True:
        game.turn("white")
        game.turn("black")

if __name__ == "__main__":
    main()
# chess board with its corresponding notation
'''
  a  b  c  d  e  f  g  h
8  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .
'''
