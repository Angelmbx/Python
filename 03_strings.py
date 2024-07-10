### Strings ###

my_string = "My String"
single_colon_string= 'Single colon String'

# len()
print(len(my_string))
print(len(single_colon_string))

# concat
print(my_string + " " + single_colon_string)

new_line_string = "Este es un string con \n salto de línea"
print(new_line_string)

tab_string= "\t Este es un String con tabulación"
print(tab_string)

scape_string = "\\t Este es un string \\n escapado"
print (scape_string)


# Formateo
name, surname, age = "Angel", "Miranda", 33
print("Mi nombre es  {} {} y mi edad es {}".format(name, surname,age)) 
print("Mi nombre es  %s %s y mi edad es %d" %(name, surname, age)) # de esta manera nos aseguramos de que imprima los datos con el tipo que realmente son ('int' en vez de 'str' p.ej)
# print("Mi nombre es  %s %s y mi edad es %d" %(name, surname, "Hola")) Así rompería, pues le estaría pasando un String en vez de un int
#inferencia de datos 
print("Mi nombre es {name} {surname} y mi edad es {age}") #asi lo imprimiría tal cual. Hace falta una f tras abrir el paréntesis
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #la mejor manera si solo queremos mostrar datos sin importar su tipo


# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a) # imprime P
print(b) # imprime y ...


# División

language_slice = language[1:3] #letras de la 1 (y) a la 3(h) sin contarla
print(language_slice) # imprime (yt)

language_slice = language[1:] #letras de la 1 (y) al final
print(language_slice) # imprime (ython)

language_slice = language[-2] #la segunda por el final
print(language_slice) # imprime (o)

reversed_language = language[::-1] # orden para imprimirlo al revés
print(reversed_language) # imprime nohtyP

language_slice = language[0:5:2] # toma del primer a último caracter (0-5) y muestra de 2 en 2(caracter 0-2-4)
print(language_slice) # imprime (Pto)


# Funciones del sistema

print(language.capitalize()) # Hace que la primera letra sea mayúsucla
print(language.upper()) # todas mayúsculas
print(language.lower()) # todas minusculas 
print(language.count("t")) # devuelve cuantas t hay en Python en este caso
print(language.isnumeric()) # si el valor de language es un número (false)
print(language.upper().isupper()) # pasa todo a mayus. y comprueba que sea mayus (true)
print(language.startswith("Py")) # es case-sensitive
