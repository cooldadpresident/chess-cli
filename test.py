def print_board(board):
    print('  a b c d e f g h')
    for i in range(8):
        print(8 - i, end=' ')
        for j in range(8):
            if (i + j) % 2 == 0:
                print(f"[{board[i][j]}]", end=" ")
            else:
                print(f"{{{board[i][j]}}}", end=" ")
        print()
