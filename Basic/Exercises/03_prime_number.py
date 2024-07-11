'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
                                                    '''
def is_prime(number):
    if number <= 1: # los números primos son aquellos mayores que 1 que solo son divisibles entre ellos y 1
      return False 
    for i in range(2,number):
      if number % i == 0:
         return False
    return True 
   
   
# Hace la comprobación e imprime todos los números primos entre 1 y 100
for number in range (0, 100):
      if is_prime(number):
         print(number)

