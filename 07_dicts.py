### Dictionaries ###

my_dict = dict()
my_other_dict = {} # dos maneras de declararlos

my_other_dict = {"Nombre":"Angel", "Apellido":"Miranda", "Edad":33, 1:"Python"} #parecido a JSON - Se pueden mezlcar tipos de clave 'str', 'int', ...

my_dict = { 
    "Nombre":"Angel", 
    "Apellido":"Miranda", 
    "Edad":33, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},# se pueden meter las estructuras anteriormente vistas en un dict, aquí un set.
    1: 1.90
}


print(my_other_dict)
print(my_dict)

# len()
print(len(my_other_dict)) # =4
print(len(my_dict)) # =5 (lo que cuenta son las claves, da igual que sean sets etc.)

## Buscar datos dentro de un diccionario
print(my_dict["Nombre"]) # = Angel. Gracias a las claves es muy sencillo buscar sus valores

print("Miranda" in my_dict) # false
print("Apellido" in my_dict) # true (busca las claves! no los valores)

## Actualizar datos
my_dict["Nombre"] = "Leticia" 
print(my_dict["Nombre"]) # = Leticia. De esta manera se actualiza el valor de la clave "Nombre"

my_dict["Calle"] = "Marques de Valterra" # se agrega un nuevo valor al diccionario
print(my_dict)

## Eliminar datos
del my_dict["Calle"] # de esta manera se elimina una clave del 'dict'. Atencion a pasarle siempre la clave o eliminarás todo el 'dict'
print(my_dict)

## Algunas funciones del sistema
print(my_dict.items()) # devuelve todos las claves + valor
print(my_dict.keys()) # todas las claves unicamente
print(my_dict.values()) # todos los valores unicamente

## Copia de diccionarios 

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Crea un nuevo diccionario con las claves que le pases aquí, pero sin valor todavía
                                                   # 'dict' es un diccionario genérico del sistema, que se llama para poder utilizar el metodo .fromkeys

print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # aquí le paso directamente otro diccionario
print(my_new_dict) # realiza una copia del diccionario pero solo con las claves. Este caso puede ser el más útil de todos

my_new_dict = dict.fromkeys(my_dict, ("Angel", "Miranda")) # de esta manera todas las claves son rellenadas con ("Angel", "Miranda")
print(my_new_dict)


