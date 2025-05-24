text_1 = input("Ingrese palabra:").lower()
text_2 = input("Ingrese texto:").lower()

found = True
start = 0

for char in text_1:
    position = text_2.find(char, start)
    if position < 0:
        found = False
        break
    start = position + 1

if found == True:
    print("Si")
else:
    print("No")
