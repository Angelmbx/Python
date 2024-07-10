### Exceptions Handling ###

number_one = 5
number_two = 6

number_two = "6"

try:
    print(number_one + number_two)
    print("Cifras sumadas satisfactoriamente")
except: 
    print("Se ha producido un error, verifique los datos introducidos")
else:
    print("La ejecución continúa correctamente") # se ejecuta si no se produce un error
finally:
    print("Muchas gracias") # se ejecuta SIEMPRE


## Captura de excepciones por tipo

# print(number_one + number_two) TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    print(number_one + number_two)
    print("Cifras sumadas satisfactoriamente")
except TypeError: 
    print("Se ha producido un TypeError") 

# esto es útil si queremos ejecutar un código distinto dependiendo del tipo de error que lance la aplicación


try:
    print(number_one + number_two)
    print("Cifras sumadas satisfactoriamente")
except TypeError as error: 
    print(error) # = unsupported operand type(s) for +: 'int' and 'str'
    # Permite recibir información del error antes de que rompa el programa, antes este mensaje te lo ponía al romper el programa
except Exception as error:
    print(error) # Exception es la excepción genérica. Sirve para recoger información del error si es uno diferente a los anteriormente contemplados