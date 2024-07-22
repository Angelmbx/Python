### File Handling ###

import os # para poder eliminar más tarde el archivo

file_path = "Intermediate/my_file.txt" # Ruta desde el directorio raíz

# Abre el archivo usando 'with' para asegurar que se cierra correctamente
# Depués de file_path, se abre en modo append "a", para poder escribir al final del fichero. Sino, sobreescribiría las primeras líneas
with open(file_path, "a") as txt_file:
    txt_file.write("\nAunque también aprendo Angular")

with open(file_path, "r+") as txt_file: # r+ para leer y escribir
    # content = txt_file.read() Lee todo el fichero
    # content = txt_file.read(10) Lee los primeros 10 caracteres
    # content = txt_file.readline() Lee primera linea
    for line in txt_file.readlines(): # Lee linea a linea
        print(line) # En los ejemplos de content sería print(content)





file2_path = "Intermediate/my_other_file.txt" # Este archivo no existe

with open(file2_path, "w+") as txt_file: # Al no existir lo crea y escribe lo que le hemos mandado
    txt_file.write("Este es otro archivo \nEl cual no existe \nPara forzar a que lo cree en la propia ejecución")

# os.remove(file2_path) # Elimina el archivo

