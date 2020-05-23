# Módulo para trabajar cona rchivos csv
import csv

# Clase de trabajo
class Contacto():
    def __init__(self, USUARIO, NOMBRE, CORREO):
        self.USUARIO = USUARIO
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO

# Lista de trabajo
Contactos = []

# Abrir y cargar datos usando como deparador: |
# Se cargan los datos en una lista de objetos <<Contactos>>
with open('contactos.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    for e in lector_csv:
        Contactos.append(Contacto(e[0],e[1],e[2]))

# Barrido de <<Contactos>>, leyendo propiedades
for o in Contactos:
    print(o.USUARIO)
    print(o.NOMBRE)
    print(o.CORREO)

# Captura de nuevos datos, se agrega un nuevo objeto de tipo Contacto
# EL onjeto de tipo Contacto puede cargarse a la colección y pasar a un archivo csv