def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    copy_board = board.copy()
    for i in range(len(copy_board)):
        for j in range(len(copy_board[i])):
            if isinstance(copy_board[i][j], (int, float)):
                free_fields.append((i, j))
    return free_fields