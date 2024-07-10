### Classes ###


class MyEmptyPerson : # definir una clase. Las clases se escriben en CamelCase!!! empezando con mayúscula.
    pass # término que sirve para evitar el error cuando no tiene contenido una clase, funcion etc.

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person: # Lo lógico sería tener un propio archivo llamado Persona.py, aquí en el mismo archivo a modo de apuntes
    def __init__(self, name, surname) -> None: # constructor de clase
        self.name = name # necesario para poder hacer my_person.name
        self.surname = surname # my_person.surname
        self.age = 33 # valor por defecto
        self.full_name = f"{name} {surname}"

    def walk(self): # self necesario para acceder a las propiedades de self. En este caso self.full_name
        print(f"{self.full_name} está caminando")

my_person = Person("Angel", "Miranda")
print(my_person.name, my_person.surname, my_person.age, my_person.full_name) # Angel Miranda 33 Angel Miranda
my_person.walk() # Angel Miranda está caminando