# Se importa el modulo datetime
import datetime
# Creación de clases. Se usa PascalCase
class Pais():
    def __init__(self, NombreIng, NombreEsp, Fallecidos, Contagiados, PDC):
        # nombreIng: Nombre del país en inglés
        # nombreEsp: Nombre del país en español
        # fallecidos: Total de fallecidos registrados en el país
        # pdc: primer día de contagio
        # contagiados: Total de contagiados registrados en el país
        self.NombreIng = NombreIng
        self.NombreEsp = NombreEsp
        self.Fallecidos = Fallecidos
        self.Contagiados = Contagiados
        self.PDC = PDC

class Incidente():
    def __init__(self, Fecha, Pais, NumContagios, NumFallecidos):
        # fecha: fecha de los datos
        # pais: país que reporta los datos
        # numContagios: nuevos contagios en presentados en fecha y pais
        # numFallecidos: nuevos fallecimientos presentados en fecha y pais
        self.Fecha = Fecha
        self.Pais = Pais
        self.NumContagios = NumContagios
        self.NumFallecidos = NumFallecidos

# Prueba de clases

# Instanciar clase pais (se crea objeto de tipo pais)
paisMx = Pais(str("Mexico"), str("México"), int(1000), int(5000), datetime.datetime(2020, 5, 18))
paisAr = Pais(str("Argentina"), str("Argentina"), int(2000), int(4000), datetime.datetime(2020, 5, 10))
paisBr = Pais(str("Brazil"), str("Brasil"), int(3000), int(6000), datetime.datetime(2020, 3, 12))
paisRu = Pais(str("Russia"), str("Rusia"), int(900), int(1000), datetime.datetime(2020, 4, 8))
paisCa = Pais(str("Canada"), str("Canada"), int(800), int(9000), datetime.datetime(2020, 5, 5))
print (paisMx.PDC)
print (paisAr.PDC)
print (paisBr.PDC)
print (paisRu.PDC)
print (paisCa.PDC)

# Instanciar clase incidente (se crea objeto de incidente)
incidenteAyer = Incidente(datetime.datetime(20, 5, 17), str("Mexico"), int(1500), int(18))
incidenteHoy = Incidente(datetime.datetime.now(), str("Mexico"), int(1400), int(12))
print (incidenteAyer.Pais)
print (incidenteHoy.Fecha)