# Escritura de archivo texto plano

# Modulo para trabajar con el sistema operativo
import os

# Modulo para trabajar con archivos csv
import csv

# Se declara clase Contacto
# <<clase Contacto>> sirve para poblar una lista que perimte manejar en memoria los datos.
# La lista se vaciía al archivo csv final del programa
class Contacto():
    def __init__(self, USUARIO, NOMBRE, CORREO):
        self.USUARIO = USUARIO
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO

# Lista para trabajar con los contactos
Contactos = []
# Se cargan dos elementos
Contactos.append(Contacto('master', 'Jose Ruiz', 'jose.ruiz@hotmail.com'))
Contactos.append(Contacto('student', 'Alma Perez', 'almitarules@hotmail.com'))
# En el programa final, la lista se carga a partir del archivo csv

# Se guarda en la variable <<ruta>> la ruta absoluta, del directorio actual de trabajo (cwd)
ruta = os.path.abspath(os.getcwd())
archivo_trabajo = ruta+"\\contactos.csv"
archivo_respaldo = ruta+"\\contactos.bak"

# Determinar si el archivo de trabajo existe
if os.path.exists(archivo_trabajo):
    # Si el archivo existe, entonces verifica si hay respaldo y lo borra
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)
    # Se establece el archivo de datos, como respaldo
    os.rename(archivo_trabajo,archivo_respaldo)

# Se genera archivo csv
f = open(archivo_trabajo, "w+")

# Escritura de encabezados de archivo csv
f.write("USUARIO|NOMBRE|CORREO\n")
# Se escribe en el archivo csv, a partir de la lista de objetos
for elemento in Contactos:
    f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

# Se cierra archivo csv
f.close()