### Higher Order Functions ###

# Funciones de orden superior = funciones que ejecutan otras funciones

# funciones clásicas:
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

# pasando función como parámetro
def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5,4, sum_one)) # = 10
print(sum_two_values_and_add_value(5,4, sum_five)) # = 14

# se pasa una función indeterminada como parámetro, la cual puede ser sustituida por distintas funciones
# en este caso utilizamos ese parámetro para usar las funciones 'sum_one' y también 'sum_five'



### Closures ###

# Closure= Funcion que define una función y retorna UNA FUNCIÓN (no un valor)

def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()
print(add_closure(5)) # = 15



### Built-in Higher Order Functions (Func de Ord Sup propias del Sistema) ###

## Map
numbers = [2, 5, 10, 21]
def multiply_two(number):
    return number * 2

# los maps devuelven un conjunto iterable que es el resultado de otro conjunto iterable al que se le aplica una función-> map(funcion, conjunto iterable)

print(map(multiply_two, numbers)) # = '<map object at 0x1028d7130>' devuelve un objeto
print(list(map(multiply_two, numbers))) # '[4, 10, 20, 42]' devuelve una lista con los valores de la lista 'numbers' multiplicados por 2

# Se puede hacer lo anterior con una LAMBDA. Simplifica mucho el código!!!
print(list(map(lambda number: number *2, numbers)))


## Filter

# Los Filter recorren un conjunto iterable y ejecuta una función que retorna 'True' o 'False' para saber cómo filtrar sus valores

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

def filter_lesser_than_ten(number):
    if number < 10:
        return True
    return False

print(filter(filter_greater_than_ten, numbers)) # vuelve a devolver un objeto
print(list(filter(filter_greater_than_ten, numbers))) # = [21] 
print(list(filter(filter_lesser_than_ten, numbers))) # = [2, 5]

# Con lambdas
print(list(filter(lambda number: number >10, numbers))) # = [21]
print(list(filter(lambda number: number <10, numbers))) # = [2, 5]


## Reduce

# Va a operar con un valor + el acumulado con los valores que de un conjunto iterable

from functools import reduce
# a diferencia de map() y filter(), para utilizar reduce() es necesario importarlo primero de functools


def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers)) # = 38 (en 'int', no lista) (lo mismo que 2 + 5 + 10 + 21)