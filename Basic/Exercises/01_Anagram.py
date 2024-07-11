'''
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
     las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
                                                        '''


### mi versión ###
def anagram_checker():
    word_1 = input("Type your first word: ")
    word_2 = input("Type your second word: ")

    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()

    word_1_length = len(word_1)
    word_2_length = len(word_2)
    letters_1_list = list()
    letters_2_list = list()
    
    if word_1_length == word_2_length:
        for letter1, letter2 in zip(word_1, word_2):

            letters_1_list.append(letter1)
            letters_2_list.append(letter2)

    else:
        print("Tus dos palabras no son anagramas") 
        


    letters_1_list.sort()
    letters_2_list.sort()
    
    if letters_1_list == letters_2_list:
        print("Enhorabuena! tus dos palabras son anagramas")
    else:
        print("Tus dos palabras no son anagramas")
     

anagram_checker()    


### versión corregida ###

'''
def anagram_checker_2():
    word_1 = input("Type your first word: ")
    word_2 = input("Type your second word: ")

    # Eliminar espacios en blanco y convertir a minúsculas
    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()

    word_1_length = len(word_1)
    word_2_length = len(word_2)

    if word_1_length != word_2_length:
        print("Tus dos palabras no son anagramas")
        return

    # Contar la frecuencia de cada letra en ambas palabras
    frequency_1 = {}
    frequency_2 = {}

    for letter in word_1:
        if letter in frequency_1:
            frequency_1[letter] += 1
        else:
            frequency_1[letter] = 1

    for letter in word_2:
        if letter in frequency_2:
            frequency_2[letter] += 1
        else:
            frequency_2[letter] = 1

    # Verificar si las frecuencias de letras son iguales
    if frequency_1 == frequency_2:
        print("Enhorabuena! Tus dos palabras son anagramas")
    else:
        print("Tus dos palabras no son anagramas")

anagram_checker_2()
'''