### Lambdas ###

# Son funciones anónimas

# Para declaralas se usa la palabra reservada 'lambda' seguida de sus parámetros, ':' y lo que hace. Permiten guardarlas en variables.
sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(2,4))


## Una lambda dentro de una función

def sum_three_values(value): 
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))
