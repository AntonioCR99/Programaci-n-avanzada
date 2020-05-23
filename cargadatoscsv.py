# Programa para leer archivos csv, y lo carga en un objeto, y lo almacena en una lista

# Libreria para acceder a archivos csv
import csv

# Libreria para manejar datos de tipo datetime
import datetime


# Clase para almacenar los incidentes
class Incidente():
    def __init__(self, FECHA, CASOS, MUERTES, PAIS):
        # FECHA: fecha de los datos
        # CASOS: nuevos contagios en presentados en fecha y pais
        # MUERTES: nuevos fallecimientos presentados en fecha y pais
        # PAIS: país que reporta los datos
        self.FECHA = FECHA
        self.CASOS = CASOS
        self.MUERTES = MUERTES
        self.PAIS = PAIS

# Lectura secuencial del archivo
with open('AnalisisCOVID19.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    # Se crea lista vacia
    lista_incidentes = []
    # Lectura secuencial
    for linea_datos in lector_csv:
        if contador_lineas == 0:
            # Si es la primer linea, muestra los nombres de campo y no guarda nada en la lista
            print(f'Los nombres de columnas son {", ".join(linea_datos)}')
        else:
            # Si son datos posteriores a la primera linea...
            # Se genera instancia de la clase Incidente, y se le proporciona al contructor los valores leidos
            #>>>>>>> Aqui se convierte el primer valor a su equivalente datetime
            objeto_temporal = Incidente({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]})
            lista_incidentes.append(objeto_temporal)

        contador_lineas += 1
    print(f'Procesadas {len(lista_incidentes)} lineas.')

    # Modificar clase para que la propiedad FECHA sea datetime, y no str
    # Proporcionar informacion contenida en {linea_datos[0]} como fecha al objeto