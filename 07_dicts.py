### Dictionaries ###

my_dict = dict()
my_other_dict = {} # dos maneras de declararlos

my_other_dict = {"Nombre":"Angel", "Apellido":"Miranda", "Edad":33, 1:"Python"} #parecido a JSON - Se pueden mezlcar tipos de clave 'str', 'int', ...

my_dict = { 
    "Nombre":"Angel", 
    "Apellido":"Miranda", 
    "Edad":33, 
    "Lenguajes": {"Python", "Swift", "Kotlin"} # se pueden meter las estructuras anteriormente vistas en un dict, aquí un set.
}


print(my_other_dict)
print(my_dict)