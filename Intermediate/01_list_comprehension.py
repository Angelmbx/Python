### List Comprehension ###

# Las listas comprimidas es una manera de crear listas de forma rápida, o en base a listas ya existentes

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_new_list = [i for i in my_original_list] # un elemento por cada elemento en la lista con la que quiera trabajar, simplemente la copia

print("-----------------------")
print("Copia: ")
print(my_new_list) # [35, 24, 62, 52, 30, 30, 17]
print("-----------------------")
print("i for i in range(5)")
my_new_list = [i for i in range(5)] 
print(my_new_list) # [0, 1, 2, 3, 4, 5, 6] range(8) para tenerla toda (8 posiciones)
print("-----------------------")
print("Lista creada directamente con un range(8) (Se copian todos los elementos)")
my_range = range(8)
print(list(my_range)) 

## Usar i for i in range para modificar listas
print("-----------------------")
my_list = [i+1 for i in range(8)]
print("i+1 for i in range 8")
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8] todos los valores +1
print("-----------------------")
print("i*3 for i in range 8")
my_list = [i*3 for i in range(8)]
print(my_list)
print("-----------------------")


print("sum_five(i) for i in range(8)")
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)] # permite crear listas utilizando funciones más o menos complejas
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12]

print("-----------------------")

