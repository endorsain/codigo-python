# Validador IBAN.

iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(" ", "")

print("iban - 1: ", iban)

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    print("iban - 2: ", iban)
    iban2 = ""
    print("iban2 - 1: ", iban2)
    for ch in iban:
        print("ch in iban: ", ch)
        if ch.isdigit():
            iban2 += ch
        else:
            print("no es digito: ", ch)
            iban2 += str(10 + ord(ch) - ord("A"))
            print(
                "dentro de iban2: ",
                str(10 + ord(ch) - ord("A")),
                "-->",
                "ord(ch): ",
                ord(ch),
                'ord("A"): ',
                ord("A"),
                "-->",
                ord(ch) - ord("A"),
            )
            print("iban2 - 2: ", iban2)
    iban = int(iban2)
    print(
        "iban - 3: ",
        iban,
        "-->",
        "int(iban2): ",
        int(iban2),
        "-->",
        "iban2 - 3: ",
        iban2,
    )
    if iban % 97 == 1:
        print("el resto de iban es: ", iban % 97, "el resultado es: ", iban / 97)
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")
