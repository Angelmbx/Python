### File Handling ###

import os # para poder eliminar más tarde el archivo

file_path = "Intermediate/my_file.txt" # Ruta desde el directorio raíz

# Abre el archivo usando 'with' para asegurar que se cierra correctamente
# Depués de file_path, se abre en modo append "a", para poder escribir al final del fichero. Sino, sobreescribiría las primeras líneas
# with open(file_path, "a") as txt_file:
#    txt_file.write("\nAunque también aprendo Angular")

with open(file_path, "r+") as txt_file: # r+ para leer y escribir
    # content = txt_file.read() Lee todo el fichero
    # content = txt_file.read(10) Lee los primeros 10 caracteres
    # content = txt_file.readline() Lee primera linea
    for line in txt_file.readlines(): # Lee linea a linea
        print(line) # En los ejemplos de content sería print(content)





file2_path = "Intermediate/my_other_file.txt" # Este archivo no existe

# with open(file2_path, "w+") as txt_file: # Al no existir lo crea y escribe lo que le hemos mandado
#    txt_file.write("Este es otro archivo \nEl cual no existe \nPara forzar a que lo cree en la propia ejecución")

# os.remove(file2_path) # Elimina el archivo


## JSON files

import json


json_file_path = "Intermediate/my_json_file.json" 

json_test = {
    "name": "Angel",
    "surname": "Miranda",
    "age": 33,
    "language": ["Python", "Swift", "Kotlin"],
    "color": "Green"
    }

with open(json_file_path, "w+") as json_file:
    json.dump(json_test, json_file, indent = 2) # Copia el contenido de json_test en json_file (my_json_file.json)
    # indent = 2, para que el archivo quede bien formateado. Si no se incluye este parámetro, el archivo se escribe en una sola línea.
    # el número que se le atribuya será el número de espacios que dejará de 'sangrado'

json_dict = json.load(open(json_file_path)) # intentar recuperar el contenido del json y convertirlo a un diccionario
print(json_dict) # = {'name': 'Angel', 'surname': 'Miranda', 'age': 33, 'language': ['Python', 'Swift', 'Kotlin'], 'color': 'Green'}
print(type(json_dict)) # <class 'dict'>

print(json_dict["name"]) # 'Angel'


## .csv files
#Los csv son ficheros estilo 'Excel'

import csv

csv_file_path= "Intermediate/my_csv_file.csv"

csv_file = open(csv_file_path, "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "color"]) # una primera fila
csv_writer.writerow(["Angel", "Miranda", 33, "Python", "Green"]) # segunda fila con los datos 
csv_writer.writerow(["María", "Suarez", 31, "Java", "Yellow"])
csv_writer.writerow(["Incomplete", "", "50", "", "Blue"])

csv_file.close()

with open(csv_file_path) as my_other_file:
    for line in my_other_file.readline():
        print(line)
        
## .xlsx files
# import xlrd # Debe instalarse el módulo
## .xml files
import xml