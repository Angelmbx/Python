### Functions ###

def my_function(): # manera de definir una función
    print("Esto es una función") #no hay llaves, entra todo lo que esté tabulado

my_function() # printea el texto 


## Funciones parametrizadas

#A)
def sum_two_values(a,b): 
    if isinstance(a,int) and isinstance(b,int): # comprobación de que los dos datos que recibe son tipo 'int'
       print(a+b) 
    else:
        print("Debe introducir dos números enteros")

sum_two_values(3,4)
sum_two_values("Hola", 7)


#B) Cambiar orden de parámetros
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Miranda", name="Angel") # posibilidad de cambiar el orden de los parámetros

#C) Valor por defecto
def print_name_with_default(name, surname, alias="Sin alias"): # Si no se pasa ningún parámetro como alias se imprimirá 'Sin alias'
    print(f"{name} {surname} {alias}")

print_name_with_default("Angel", "Miranda", "Angelmbx")

#D) Indeterminado número de parámetros (1 o +)
def print_text(*text): # al poner el * hace que pueda recibir un ilimitado numero de parámetros
    print(text) # sin for: ('Hola', 'Ramón', 'Hala Celta!')

def print_upper_texts(*texts): # al poner el * hace que pueda recibir un ilimitado numero de parámetros
    for text in texts:
        print(text.upper()) #con este bucle for imprime cada texto en una línea
        # imprime todo el texto que recibe y lo convierte en mayúsculas

print_upper_texts("Hola", "Ramón", "Hala Celta!")

## Funciones con return
def sum_two_values_with_return(a, b):
    return a + b


my_result = sum_two_values_with_return(5,6) # asigno el resultado de la función a una variable
print(f"Con return:  {my_result}")


