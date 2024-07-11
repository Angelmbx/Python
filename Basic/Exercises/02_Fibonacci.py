'''
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
    - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
                            '''

# primeros dos números de la sucesión de Fibonacci
a = 0
b = 1
numbers = [a, b]

# Añade números a la lista hasta que esta tenga un tamaño de 50
while len(numbers) < 50:
    next_number = a + b
    numbers.append(next_number)
    a, b = b, next_number # a toma el valor de b, y b el de next_number


# Imprime los 50 números acompañados de un índice que empieza en 1
for index, number in enumerate(numbers):
    print(f"{index + 1}: {number}")

