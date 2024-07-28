### Regular expressions ###

# Las E.R. inspeccionan cadenas de texto

import re

my_string = "Esta es la lección número 6: Lección llamada Expresiones regulares"
my_other_string = "Esta no es la lección número 5: Manejo de ficheros"

## match() -> Comprueba si la cadena comienza con el patrón especificado
print(re.match("Esta es la lección", my_string, re.I)) # re.I -> Ignora las may o minusc, hay otras dentro de re.
print(re.match("Esta es la lección", my_other_string)) # None -> No comienza así
print(re.match("Expresiones regulares", my_string)) # None -> Aunque ese texto existe en la cadena, no empieza así

match_result = re.match("Esta es la lección", my_string, re.I)
print(match_result)
start, end = match_result.span()
print(my_string[start:end]) # Devuelve la cadena la cual constituye el match "Esta es la lección"

# Que pasa si hacemos esto último con algo que devuelva un None? Error. Por lo tanto, conviene hacer una comprobación:

match_result = re.match("Esta es la lección", my_other_string)
# if match_result != None: Otra manera
# if not match_result == None: Otra manera
if match_result is not None:
    print(match_result)
    start, end = match_result.span()
    print(my_other_string[start:end])  # No imprime nada ya que devuelve None

match_result = re.match("Esta no es la lección", my_other_string)
# if match_result != None: Otra manera
# if not match_result == None: Otra manera
if match_result is not None:
    print(match_result)
    start, end = match_result.span()
    print(my_other_string[start:end]) # Imprime "Esta no es la lección"


## search() -> encuentra la cadena enviada en cualquier parte de la cedena, no solo al comienzo

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end]) # Devuelve "lección"

## findall() -> devuelve todas las veces que se encuentra la cadena que le pasamos en la cadena origen

findall = re.findall("lección", my_string, re.I)
print(findall) # ['lección', 'Lección']

## split() -> Separa una cadena de texto en dos partes, devolviendo una lista de dos elementos que son cadenas de texto

print(re.split(":", my_string)) # Se le pasa en qué momento quieres separarla y la cadena a separar
# ['Esta es la lección número 6', ' Lección llamada Expresiones regulares']

## sub() -> Sustituye la cadena que escribimos en primer lugar por la segunda

print(re.sub("Expresiones", "patatas", my_string))
# Esta es la lección número 6: Lección llamada patatas regulares
print(re.sub("lección|Lección", "pelota", my_string)) # cambia ambas concurrencias
# Esta es la pelota número 6: pelota llamada Expresiones regulares

