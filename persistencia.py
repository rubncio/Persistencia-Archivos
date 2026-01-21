import json
import os


def read(rutaArchivo): 
    #deserializar 
    with open(rutaArchivo, "r") as archivo:
        return json.load(archivo)
        
def update(rutaArchivo, contenido): 
    #serializar
    with open(rutaArchivo, "w") as archivo:
        json.dump(contenido, archivo, indent=4 )

def write(rutaArchivo, contenido): 
    #serializar
    with open(rutaArchivo, "a") as archivo:
        json.dump(contenido, archivo, indent=4)
        

def clear(rutaArchivo): 
    with open(rutaArchivo, "w") as archivo:
        archivo.write("")

def delete(rutaArchivo): 
    os.remove(rutaArchivo)

if __name__=="__main__":
    """write("data/usuarios.json",[{"id": 5,
  "nombre": "angela",
  "email": "ana@ejemplo.com"},
  {"id": 6,
  "nombre": "alejandra",
  "email": "ana@ejemplo.com"},
  {"id": 7,
  "nombre": "alex",
  "email": "ana@ejemplo.com"}])"""
    clear("data/usuarios.json")