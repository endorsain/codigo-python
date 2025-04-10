from make_list_of_free_fields import make_list_of_free_fields

def number_per_free_field(board, number):
    if number < 0 or number > 9:
        return False
    field = None
    free_fields = make_list_of_free_fields(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if number == (i*3)+j+1:
                field = (i, j)
                if field in free_fields:
                    return field
    return False