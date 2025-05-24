word1 = input("Ingrese 1er palabra: ")
word2 = input("Ingrese 2da palabra: ")

word1 = word1.lower().replace(" ", "")
word2 = word2.lower().replace(" ", "")

if len(word1) > 1 and len(word2) > 1:
    anagram = True

    while anagram:
        for char in word1:
            count_word = word1.count(char) == word2.count(char)
            if not count_word:
                anagram = False
                break
        break

    if anagram:
        print("Anagramas")
    else:
        print("No son anagramas")
else:
    print("No son anagramas")

# Otra opcion...

# saca los espacios y convierte la cadena a minusculas
word1 = word1.lower().replace(" ", "")
# covierte el string en una lista
word1 = list(word1)
# ordena la lista alfabeticamente
word1 = sorted(word1)
# une la lista en una nueva cadena
word1 = "".join(word1)

word2 = "".join(sorted(list(word2.lower().replace(" ", ""))))

if len(word1) > 0 and word1 == word2:
    print("Anagramas")
else:
    print("No son anagramas")
