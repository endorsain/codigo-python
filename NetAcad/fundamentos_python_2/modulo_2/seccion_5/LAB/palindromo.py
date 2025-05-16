text = input("Ingresa palindromo: ")

new_text = ""

text.lower()
text.replace(" ", "")

new_text = text[::-1]

if len(text) > 1 and text == new_text:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")
