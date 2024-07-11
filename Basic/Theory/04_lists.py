### Lists ####

my_list = list()
my_other_list = [] # dos maneras distintas de declararlas

my_list = [33, 30, 39, 30, 22, 26, 29]

print(my_list)
print(len(my_list)) # resultado = 7

my_other_list = [33, 1.90, "Angel", "Miranda"] # se pueden guardar distintos tipos de datos en una lista

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # ultimo elemento de la lista
print(my_other_list[-3]) # tercero contando desde atrás

## Count()
print(my_other_list.count("Angel")) # = 1
print(my_list.count(30)) # = 2


## Asignar los valores de una lista a unas variables
age, height, name, surname = my_other_list # Las variables deben estar en el orden deseado
                                           # Debe haber tantas variables como elementos, o da error.
print(name) # = "Angel"


## ¿Se pueden sumar listas? Sí
print(my_list + my_other_list) # resultado = una sola lista con los valores de la lista1+lista2 concatenados


## Añadir elementos a una lista
my_other_list.append("Vigo") # añade siempre al final
my_other_list.insert(3, "Verde") # permite indicar en que posición insertar el nuevo valor


## Eliminar elementos de una lsita

#A)
my_other_list.remove("Miranda")
print(my_other_list)

my_list.remove(30)
print(my_list) # Había dos 30 en esa lista, solo elimina uno (el primero que encuentra)

#B)
my_list.pop() # elimina el ultimo elemento de la lista
# si antes de eliminar lo printeas print(my_list(pop())) te devuelve qué elemento se eliminaría
my_list.pop(2) # elimina el elemento ubicado en la posición 2 de la lista

my_pop_element = my_list.pop(2) # guarda en una variable el elemento que desacoplamos de la lista

#C)
del my_list[2] # elimina el elemento en la posición 2

# La diferencia entre pop y del, es que del solo lo elimina, mientras que pop lo elimina y te lo devuelve (permite almacenarlo en un valor)
# Diferencia entre del y remove: del elimina por indice, y remove elimina un elemento que sabes que está en la lista (si hay varios, el 1º que encuentre)

#D)
my_list.clear() # elimina todos los elementos de la lista


## Modificar un elemento de la lista

# anteriormente: my_other_list.insert(3, "Verde")
my_other_list[3] = "Azul"

## Copiar listas
my_list.append("Dato1")
my_list.append("Dato2")
my_list.append("Dato3")

my_new_list = my_list.copy()
my_list.clear()
print(my_new_list)
print(my_list)

## Reverse()
my_new_list.reverse()
print(my_new_list) # valores ordenados al revés

## Sort()
my_new_list.sort() #vuelve al orden alfabético o numérico de menor a mayor en caso de numeros por defecto
print(my_new_list) # Antes Dato3, Dato2, Dato1 ; ahora Dato1, Dato2, Dato3

##Sublistas
print(my_new_list[1:2]) # entre el elemento 1 y 2 = ['Dato2']
print(my_new_list[0:1]) # ['Dato1']

