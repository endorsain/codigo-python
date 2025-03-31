from random import randrange
from make_list_of_free_fields import make_list_of_free_fields
from number_per_free_field import number_per_free_field
from display_board import display_board
from victory_for import victory_for
from enter_move import enter_move

board = [[(i * 3) + j + 1 for j in range(3)] for i in range(3)]

finish = True
turn = 'X'
board[1][1] = 'O'
display_board(board)
while True:
    if turn == 'X':
        user = enter_move(board)
        if user == False:
            break
    else:
        while True:
            computer_value = randrange(1, 10)
            field = number_per_free_field(board, computer_value)
            if field == False:
                continue
            board[field[0]][field[1]] = 'O'
            break
    
    display_board(board)
    victory = victory_for(board, turn)
    if victory == True:
        if turn == 'X':
            print('Has ganado!')
        else:
            print('Perdiste contra una computadora!')
        break
    else:
        field = make_list_of_free_fields(board)
        if len(field) == 0:
            print('Empate!')
            break
        turn = 'O' if turn == 'X' else 'X'



                


    