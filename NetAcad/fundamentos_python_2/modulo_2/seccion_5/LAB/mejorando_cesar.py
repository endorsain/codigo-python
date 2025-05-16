# a: 97 z: 122 --- A: 65 Z: 90 --- espacio: 32

text = input("Ingresa texto: ")
shift_value = int(input("ingresa valor de 1 a 25: "))

code_a = ord("a")
code_A = ord("A")


def shifted(char, code, vl):
    return (ord(char) - code + vl) % 26 + code


def cipher(txt, vl):
    result = ""
    for char in txt:
        if char.islower():
            result += chr(shifted(char, code_a, vl))
        elif char.isupper():
            result += chr(shifted(char, code_A, vl))
        else:
            result += char
    return result


print(cipher(text, shift_value))
