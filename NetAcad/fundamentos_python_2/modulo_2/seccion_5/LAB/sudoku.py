numbers = input("Ingresa los 81 numeros: ")

# [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]] 3X3
# Reviso la cadena cada 9 subcadenas(filas).
# Reviso la cadena cada 1 subcadena saltando 2 subcadenas(columna).
# Reviso la cadena cada 3 subcadenas saltando 6 subcadenas(cuadrado).
sudoku = True

row = ""
column = ""
block = ""

print("--filas--")
for char in numbers:
    row += char
    if len(row) == 9:
        print("row: ", row)
        if len(set(row)) < len(row):
            sudoku = False
            break
        row = ""
        continue

print("--columnas--")
for i in range(9):
    for j in range(i, len(numbers), 9):
        column += numbers[j]
        if len(column) == 9:
            print("column: ", column)
            if len(set(column)) < len(column):
                sudoku = False
                break
            column = ""
            continue
    if sudoku == False:
        break

print("--bloques--")
for i in range(0, len(numbers), 27):
    # print("i: ", i, "|", "numbers[i]: ", numbers[i])
    for j in range(i, 9, 3):
        # print("j: ", j, "|", "numbers[j]: ", numbers[j])
        for k in range(j, j + 3):
            # print("k: ", k, "|", "numbers[k]: ", numbers[k])
            block += numbers[k]
            if len(block) % 3 != 2:
                block += numbers[k + 9]
                block += numbers[k + 18]
            if len(block) == 9:
                # print("block: ", block)
                if len(set(block)) < len(block):
                    sudoku = False
                    break
                block = ""
                continue
        if sudoku == False:
            break
    if sudoku == False:
        break

if sudoku == True:
    print("Si")
else:
    print("No")
