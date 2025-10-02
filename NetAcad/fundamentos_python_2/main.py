def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            assert value > min and value < max
            return value
            # break
        except AssertionError:
            print(f"Error: El valor no esta dentro del rango permitido({min}...{max})")
        except:
            print("Error: Entrada incorrecta.")


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
