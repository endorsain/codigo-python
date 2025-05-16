text = input("Ingresa tu mensaje: ")
cipher = ""
descrip = ""


def cripRom(txt):
    global cipher
    for char in txt:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        # print('char: ', char, 'ord: ', ord(char), '-->', 'char: ', chr(code), 'ord + 1: ', code)
        if code > ord("Z"):
            code = ord("A")
        cipher += chr(code)
    return cipher


def descripRom(crip):
    global descripCIP
    for char in crip:
        code = ord(char) - 1
        if code < ord("A"):
            code = ord("Z")
        descrip += chr(code)
    return descrip


print(cripRom(text))
print(descripRom(cipher))
