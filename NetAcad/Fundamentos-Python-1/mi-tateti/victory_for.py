def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    tic_tac_toe = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != sign:              
                tic_tac_toe = 0
                break
            tic_tac_toe += 1
            if tic_tac_toe == 3:
                return True
    if tic_tac_toe != 3:
        tic_tac_toe = 0
    
    possible_columns = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == sign:
                if i == 0:
                    tic_tac_toe = 1
                    possible_columns.append(j)
                elif i > 0 and j in possible_columns:
                    tic_tac_toe = 2 if i == 1 else 3
            else:
                if j in possible_columns:
                    possible_columns.remove(j)
                # break
                continue
    if tic_tac_toe == 3:
        return True
    elif tic_tac_toe != 3:
        tic_tac_toe = 0
    
    full_corners = []
    if board[1][1] != sign:
        return False
    for i in range(0, len(board), 2):
        for j in range(0, len(board[i]), 2):
            if board[i][j] == sign:
                if i != 0 and len(full_corners) == 0:
                    return False
                if i == 0:
                    full_corners.append(j)
                if i == 2:
                    if len(full_corners) == 2:
                        return True
                    elif j == 0 and full_corners[0] == 2:
                        return True
                    elif j == 2 and full_corners[0] == 0:
                        return True
            continue
    # No hace falta asignarle valor a tic_tac_toe en las diagonales.                
    return False