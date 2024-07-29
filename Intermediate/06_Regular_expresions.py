### Regular expressions ###

# Las E.R. inspeccionan cadenas de texto en busca de un determinado patrón. Para poder utilizarlas es necesario importar el modulo 're'

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



## Patterns ##

pattern =  r'[lL]ección' # Lección con minúscula y mayúscula
print(re.findall(pattern, my_string)) # ['lección', 'Lección']

pattern =  r'[lL]ección|Expresiones' # Lección con minúscula y mayúscula y 'Expresiones'
print(re.findall(pattern, my_string)) # ['lección', 'Lección', 'Expresiones']

pattern =  r'[a-z]' # todas las letras de la cadena 
print(re.findall(pattern, my_string)) # ['s', 't', 'a', 'e', 's', ...]

pattern =  r'[0-9]' # numeros del 0 al 9
print(re.findall(pattern, my_string)) # ['6'] (... lección 6:)

pattern =  r'[0-5]' # numeros del 0 al 5
print(re.findall(pattern, my_string)) # []

# Aparte del findall() se pueden usar cualquiera de los vistos anteriormente. Search:
pattern =  r'[0-9]' # numeros del 0 al 9
print(re.search(pattern, my_string)) # Entre el caracter 26 y 27 ha encontrado el numero 6: <re.Match object; span=(26, 27), match='6'> 

pattern =  r'\d' # cualquier número
print(re.findall(pattern, my_string)) # ['6']

pattern =  r'\D' # todos los caracteres excepto los números
print(re.findall(pattern, my_string)) # ['E', 's', 't', 'a', ' ', 'e', 's', ' ', ... ]

pattern =  r'[l].' # todos las eles y la siguiente letra
print(re.findall(pattern, my_string)) # ['la', 'le', 'll', 'la']

pattern =  r'[l].*' # toda la cadena desde la primera ele
print(re.findall(pattern, my_string)) # ['la lección número 6: Lección llamada Expresiones regulares']


### Todas estas expresiones regulares se pueden combinar para encontrar un resultado muy concreto ###


## email validation regular expression 

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # ^ -> empieza por. Pattern = Cadena que empiece por cualquier letra A-Z mayuscula o minuscula, numeros del 0 - 9 y los caracteres _ . + o -
    # + un arroba seguido de cualquier letra mayusc o minusc y numero de 0 a 9 
    # /. La barra sirve para escapar el punto, ya que el punto puede tener un significado en las expresiones regulares y queremos que haya un punto literalmente
    # Despues del punto, cualquier letra minus o mayusc y numeros del 0 al 9 y guión o punto
    # el + después de cada corchete significa que debe haber uno o más de los caracteres incluidos en cada conjunto
    # el $ indica el final del String, y asegura que la coincidencia llegue hasta el final de la cadena
    if re.match(pattern, email):
        return True
    
    return False

correo = "angel@angel.com"

print(is_valid_email(correo)) # True

correo_2 = "correo.com"

print(is_valid_email(correo_2)) # False


### Para validar y comprobar expresiones regulares se puede visitar regex101.com una web dedicada a eso