def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    # print(board)
    print('+-------+-------+-------+')
    for i in range(len(board)):
        print('|', end='')
        for j in range(len(board[i])):
            print('       |', end='')
        print()
        print('|', end='')
        for j in range(len(board[i])):
            print(f'   {board[i][j]}   |', end='')
        print()
        print('|', end='')
        for j in range(len(board[i])):
            print('       |', end='')
        print()
        print('+-------+-------+-------+')