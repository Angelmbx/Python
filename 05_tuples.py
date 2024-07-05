### Tuples ###

my_tuple = tuple()
my_other_tuple = () # dos formas distintas de declararlas

# Una tupla es un conjunto de valores INMUTABLES

my_tuple = (33, 1.90, "Angel", "Miranda")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1]) # mismo comportamiento que listas

print(my_tuple.count("Angel"))
print(my_tuple.index("Miranda")) # poisicion 3

# my_tuple[1] = 1.94  Error. No se pueden cambiar los valores de una tupla
# my_tuple[5] = 1.05  Error
# print(my_tuple)

### La principal diferencia entre tuplas y listas es que los valores de las tuplas son inmutables ###
### no se pueden modificar los valores una vez creadas, ni añadir nuevos etc ###

my_other_tuple = (33, 50, 30)

# Sin embargo sí se pueden sumar dos tuplas para crear una sola
print(my_tuple + my_other_tuple) # valores de ambas tuplas concatenadas

my_sum_tuple = my_tuple + my_other_tuple

## Slices
print(my_sum_tuple[3:6]) # Elementos del 3 al 6


### Aunque haya maneras de llegar a modificar tuplas, el motivo de elegir una tupla es que sea inmutable ###
### Si quieres usar una tupla mutable, es más razonable utilizar una lista ###

my_tuple = list (my_tuple)
print(type(my_tuple)) #convirtiendo una tupla en una lista

my_tuple[3] = "Vigo"
my_tuple.insert(1, "Verde") # distintas operaciones con listas

my_tuple = tuple(my_tuple) # se reconvierte a tupla
print(type(my_tuple)) # tipo 'tuple'

### En un programa, usar elementos inmutables puede hacer nuestro codigo mas seguro y robusto ###
### Para cambiarla puntualmente se puede convertir en lista para volver a convertirla a tupla ###

## Borrar tuplas
del my_tuple # no es un 'clear', BORRA DIRECTAMENTE LA VARIABLE
print(my_tuple) # Error, my_tuple ya no existe