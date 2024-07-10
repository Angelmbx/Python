### Operadores ###

print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (10 % 2) # operador de módulo. Devuelve el resto de la división
print (10 // 3) # división que otorga siempre el número entero más próximo
print (2 ** 3) # dos elevado a 3, (2x2x2)  

print ("Hola " + "Python") # concatenación de Strings
print ("Hola " + str(5)) # sin str() produce un error. No se puede 'str' + 'int'
print ("Hola"*3) # imprime Hola 3 veces concatenadas

my_float = 2.5 * 2
print ("Hola " * int(my_float))



### Operadores comparativos ###

print("---- Comparando números ----")
print(3 < 4)
print(3 > 4)
print(3 <= 4)       # devuelven 'true' o 'false'
print(3 >= 4)
print(3 == 4)
print(3 != 4)

print("---- Comparando Strings ----")  # Ordenación alfabética por ASCII
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" == "Python")
print("Hola" == "Hola") # resultado = true
print("aaaa" == "bbbb") # false
print(len("aaaa") == len("bbbb")) # true, para comparar numero de caracteres se utiliza len()
print("AAAA" >= "aaaa") # false. Es sensitive case, y utiliza el orden ASCII



### Operadores lógicos -- and, or, not ###

print("---- Operadores lógicos ----")
print(3 > 5 and "Hola" > "Python") # no son las dos true (ambas falsas), resultado = false
print(3 > 5 or "Hola" > "Python")  # ninguna de las dos es true, resultado = false
print(not(3 > 5)) # 3>5=false, negar la condicion -> not(3>5) = true