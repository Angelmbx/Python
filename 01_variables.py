# Variables

MyVariable = "New string"
print(MyVariable)

# convencion = escribir las variables en snake_case

my_variable = "Really new string"
print(my_variable)


# convertir int a str
number = 5
print(type(number)) # tipo 'int'

number_to_str = str(number) # transforma variable a tipo 'str'
print(type(number_to_str))

# Algunas funciones del sistema
print(len(number_to_str)) #len = length
print(len(my_variable))

# Variables en una sola línea * Se puede hacer, aunque es un foco de errores. Dificulta el mantenimiento del código * 
name, surname, alias, age = "Angel", "Miranda", "Angelmbx", 33 # no son todo Strings.
print(name, age, alias, "Y mi apellido es: ", surname)
print(type(age)) # tipo 'int'

# Inputs
first_name = input("What is your name? ")
age = input("How old are you? ")

print(first_name)
print(age)

# ¿Forzamos el tipo de una variable?
address: str = "My address"
address = 32
print(address) # Imprime 32, toma el último valor
print(type(address)) # Es 'int', no 'str' !!! De nada sirve haber puesto :str antes. Quizás en un input tendría más sentido.



