### Modules ###

# para acceder a funciones que se encuentren en otros ficheros, primero debemos asegurarnos 
# de que ambos ficheros se encuentren en el mismo proyecto, y, después importar 
# dicho fichero para poder acceder a sus funciones

#import module 
# import 10_functions esta no se puede importar ya que comienza con un numero y da error en python
from module import print_value

# module.sum_value(5, 4, 7) así cuando importas la clase entera

print_value("Jeremías") # así cuando solo importas la función

## Importar módulos creados por el sistema

from math import pi as PI_VALUE
import random

print(PI_VALUE)
print(random.randint(0,100))