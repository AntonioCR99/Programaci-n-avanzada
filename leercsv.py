# Programa para leer archivos csv

# Libreria para acceder a archivos csv
import csv

# with genera bloque de código con referencia
# Cuando se escriba archivo_csv se trabajara con el contenido del archivo AnalisisCOVID19.csv
with open('AnalisisCOVID19.csv') as archivo_csv:
    # Se habilita objeto que permitira leer de manera secuencial el contenido del archivo csv
    # archivo_csv es el puente entre el programa y el archivo
    # lector_csv es el flujo de datos entre el programa y el archivo
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    # Contador de lineas
    contador_lineas = 0
    # Lee secuencialmente el archivo usando el flujo de datos (lector_csv)
    # La linea se coloca en el elemento linea
    # Al trabajar con <<linea_datos>> se trabaja con la linea del archivo
    # for dejará de leer cuando los datos del archivo se hayan terminado
    for linea_datos in lector_csv:
        # Si el contador es igual a cero: se encuentra en la primera linea (linea de encabezados o nombres de campo)
        if contador_lineas == 0:
            # Genera lista de todos los datos contenidos en linea_datos separados por ","
            print(f'Los nombres de columnas son {", ".join(linea_datos)}')
        else:
            # Muestra, dato por dato, los obtenidos en linea_datos
            print(f'\tFECHA: {linea_datos[0]}.')
            print(f'\tNUEVOS CONTAGIOS: {linea_datos[1]}.')
            print(f'\tNUEVOS FALLECIMIENTOS: {linea_datos[2]}.')
            print(f'\tPAÍS: {linea_datos[3]}.')
            print(f'\t----------------------------------------')
        # Se incrementa el número de lineas sin importar las condiciones
        contador_lineas += 1
    print(f'Procesadas {contador_lineas} lineas.')