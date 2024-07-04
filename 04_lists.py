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

# Count()
print(my_other_list.count("Angel")) # = 1
print(my_list.count(30)) # = 2


# Asignar los valores de una lista a unas variables
age, height, name, surname = my_other_list # Las variables deben estar en el orden deseado
                                           # Debe haber tantas variables como elementos, o da error.
print(name) # = "Angel"


# ¿Se pueden sumar listas? Sí
print(my_list + my_other_list) # resultado = una sola lista con los valores de la lista1+lista2 concatenados