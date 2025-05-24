date = input("Ingrese fecha de cumpleaños(DDMMAAAA): ")

date = date.replace(" ", "")
list_date = []

digit = 0

for char in date:
    list_date.append(int(char))

print("date: ", date)
while True:
    print("list_date: ", list_date)
    for num in list_date:
        digit += num
    print("digit: ", digit)
    if digit <= 9:
        break
    else:
        list_date = []
        digit = str(digit)
        for char in digit:
            list_date.append(int(char))
        digit = 0

print(digit)


# Otra forma MUCHO MAS optima...

date = input("Ingrese fecha de nacimiento: ")
while len(date) > 1:
    the_sum = 0
    for dig in date:
        the_sum += int(dig)
    date = str(the_sum)

print(date)
