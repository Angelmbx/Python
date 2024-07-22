### Error Types ###

## SyntaxError
# print "Hola a todos!" Error
print("Hola a todos!")

## NameError
# print(number) NameError: name 'number' is not defined -> Variable no definida previamente
number = 7
print(number)

## IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascrpit"]
# print(my_list[8]) IndexError: list index out of range
print(my_list[3])
print(my_list[-1])

## ModuleNotFoundError
# import maths ModuleNotFoundError: No module named 'maths' -> No encuentra el módulo a importar
import math

## AttributeError
# print(math.PI) AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'? -> No encuentra el atributo en el módulo a importar
print(math.pi)

## ImportError
# from math import PI ImportError: cannot import name 'PI' from 'math'
from math import pi

## KeyError
my_dict = { 
    "Nombre":"Angel", 
    "Apellido":"Miranda", 
    "Edad":33, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},# se pueden meter las estructuras anteriormente vistas en un dict, aquí un set.
    1: 1.90
}

print(my_dict["Edad"])
# print(my_dict["Apelido"]) KeyError: 'Apelido'

## TypeError
# print(my_list["Nombre"]) TypeError: list indices must be integers or slices, not str -> Las posiciones de las listas solo se pueden acceder a través de 'int' o slices
print(my_list[0])

## ValueError
# my_int = int("10 Años") ValueError: invalid literal for int() with base 10: '10 Años'
my_int = int("10")
print(my_int)

## ZeroDivisionError
#print(4/0) ZeroDivisionError: division by zero
print(4/2)