from number_per_free_field import number_per_free_field

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    user_field = None
    while True:
        try:
            value = input('Ingrese tu movimiento: ')
            int_value = int(value)
            if int_value == 10:
                return False

            user_field = number_per_free_field(board, int_value)
            
            if user_field == False:
                raise ValueError('Elije un valor que no este ocupado.')
            
            board[user_field[0]][user_field[1]] = 'X'
            return True
        except ValueError as e:
            print(f'Error: {e}')
            continue