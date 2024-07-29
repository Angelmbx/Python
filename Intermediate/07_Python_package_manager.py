### Python Package Manager ###

'''
Cuando quiero trabajar con ciencia de datos por ejemplo, y necesito utilizar una librería que no está dentro de Python
o me han hablado de un módulo que hace una cosa determinada y quiero probarlo, es necesario importar paquetes

Para ello, utilizamos una herramienta de Python llamada PIP https://pypi.org

En este caso importaremos numpy, una bibilioteca que amplia las funcionalidades básicas de python para realizar operaciones númericas más complejas
(Para instalar numpy en mi caso, tuve que crear un entorno virtual en mi macOS y seleccionar ese entorno para este proyecto mediante el python: select interpreter)
'''
import numpy # pip install numpy



numpy_array = numpy.array([35, 24, 62, 52, 30, 30,17])

print(type(numpy_array)) # <class 'numpy.ndarray'>

print(numpy_array * 2) # [ 70  48 124 104  60  60  34]


import pandas # pip install pandas || Otra biblioteca fundamental para el análisis y manipulación de datos.

# pip list, lista todas las librerias y paquetes instalados
'''
Package            Version
------------------ -----------
certifi            2024.7.4
charset-normalizer 3.3.2
idna               3.7
numpy              2.0.1
panda              0.3.1
etc.
'''

# pip uninstall pandas -> desinstala paquete

# pip show numpy -> Muestra versión, para qué sirve, etc. Una especie de 'prospecto'.

import requests # pertenece a pandas

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10") # 5 primeros pokemon
'''
print(response) # <Response [200]>
print(response.status_code) # 200. Codigo 200, recibe respuesta correctamente
print(response.json())
'''

if response.status_code == 200:
    data = response.json() # guardamos el .json de la respuesta al completo en la variable data

    pokemons = data.get('results', [])

    for index, pokemon in enumerate(pokemons, start= 1): # para añadir un indice autoincrementa al lado de cada pokemon
        print(f"{index}- {pokemon['name']}")
else:
    print(f"Error {response.status_code}: No se pudo obtener la información")

    '''
1- bulbasaur
2- ivysaur
3- venusaur
4- charmander
5- charmeleon
6- charizard
7- squirtle
8- wartortle
9- blastoise
10- caterpie
    '''


## Arithmetics from My_package_01 Package

from my_package_01 import arithmetics

print(arithmetics.sum(45,30))  # 75


## Other_arithmetics from My_package_02 Package

from my_package_02 import other_arithmetics

print(other_arithmetics.sum(4,4)) # 8