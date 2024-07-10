### Sets ###

my_set = set()
my_other_set = {} # dos formas distintas de declararlos

print(type(my_other_set)) # inicialmente dice que es un 'dict' (diccionario)

my_other_set = {"Angel", "Miranda", 33}
print(type(my_other_set)) # ahora ya dice que es de tipo 'set'

print(len(my_other_set)) # =3

## Modificación de datos

my_other_set.add("Angelmbx")
print(my_other_set) # un set no es una estructura ordenada, no se puede acceder al elemento [0], [1], ...

my_other_set.add("Angelmbx")
print(my_other_set) # hemos añadido otro "Angelmbx", sin embargo solo muestra uno. Un set NO ADMITE REPETIDOS

# Comprobar si un elemento está en el set:
print("Miranda" in my_other_set) #true
print("Miranddddd" in my_other_set) #false

# Borrar elemento
my_other_set.remove("Miranda")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set)) # = 0

del my_other_set # borra directamente el objeto! != de 'clear'. Hacer print después = error

my_set = {"Angel", "Miranda", 33}
my_list = list(my_set)
print(my_list[0]) # No es recomendable hacer esto para acceder al elemento de la posición 0, ya que en cada ejecución será un elemento distinto

# ¿Como unir dos sets?
my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_new_set = my_set.union(my_other_set) 
print(my_new_set) # Pese a hacerlo dos veces muestra 6 elementos en vez de 12, ya que LOS SETS NO ACEPTAN DUPLICADOS


seti = my_new_set.union({"JavaScript", "C#"}) # otra forma de añadir elementos
print(seti) # {33, 'C#', 'Python', 'Swift', 'Miranda', 'Kotlin', 'Angel', 'JavaScript'}

print(my_new_set.difference(my_set)) # muestra los elementos diferentes


# ¿CUANDO USAR UNA LISTA? = Quiero una estructura mutable y que admita repetidos
# ¿TUPLAS? = Quiero una estructura inmutable
# ¿SETS? = Estructura que no admita repetidos (tener en cuenta que es una estructura desordenada)