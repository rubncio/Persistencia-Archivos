import json
import os


def read(rutaArchivo)->dict: 
    #deserializar 
    with open(rutaArchivo, "r") as archivo:
        jsonString=archivo.read()
        return json.load(jsonString)
def update(rutaArchivo, contenido): 
    #serializar
    with open(rutaArchivo, "w") as archivo:
        diccionariosString= json.dump(contenido)
        archivo.write(diccionariosString)
def write(rutaArchivo, contenido): 
    #serializar
    with open(rutaArchivo, "a") as archivo:
        diccionariosString= json.dump(contenido)
        archivo.write(diccionariosString)

def clear(rutaArchivo): 
    with open(rutaArchivo, "w") as archivo:
        archivo.write("")

def delete(rutaArchivo): 
    os.
if __name__="__main__":
