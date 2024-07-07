### Loops ###

## While

my_condition = 1

while my_condition <= 10:
    print(my_condition)
    my_condition += 1
else:
    print("La condición ha llegado a 10")
    # Python permite añadir un else a los bucle while, que se ejecuta una vez se deje de cumplir la condición


while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("Se detiene la ejecución")
        break # se detiene al llegar a 15, aunque siga cumpliendo la condición hasta 20
    print(my_condition)


## For

my_list =  ["Elemento1", "Elemento2", "Elemento3", "Elemento4", "Elemento5"]

print("----- For -----")
for element in my_list:
    print(element)
 
my_tuple = (33, 1.90, "Angel", "Miranda")
my_set = {"Angel", "Miranda", 33}
my_dict = { 
    "Nombre":"Angel", 
    "Apellido":"Miranda", 
    "Edad":33, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},# se pueden meter las estructuras anteriormente vistas en un dict, aquí un set.
    1: 1.90
}

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

for element in my_dict:
    print(element) # imprime solo las claves, no los valores


# para ver los valores del 'dict'

for element in my_dict.values():
    print(element) # muestra los valores
else: 
    print("El bucle for de los valores ha finalizado")

# Igual que en While, se puede detener un bucle For
for element in my_dict:
    print(element) # no muestra "Lenguajes" ni "1" porque para al llegar a "Edad"
    if element == "Edad":
        break 
    # al llegar al break sale del bucle For. Nada de lo que haya por debajo dentro del bucle se ejecutará

