import datetime

def main():
  _strdato=input("ingresa un dato de tipo string: ")#solo se almacenan caracteres por lo tanto si se ingrea un numero este no puede usarse para operaciones matematicas a menos de que se haga una conversion 
  
  _edato=input("ingresa un dato entero: ")
  edato=int(_edato)#proceso necesario para asignarle un valor a lo que se pide en la variable anterior 

  _ddato=input("ingresa un dato tipo float: ")
  ddato=float(_ddato)

  _dtdato = input("Dame una fecha yyyy/mm/dd: ")

  # [n,m] Extrae de la posición n a la posición m,sin incluir m.

  # [-m:] Extrae desde la posición m, de atrás para adelante, hasta el final.



  anio=_dtdato[0:4]

  mes=_dtdato[5:7]

  dia=_dtdato[-2:]

  print(anio)

  print(mes)

  print(dia)

  dtdato = datetime.datetime(int(anio), int(mes), int(dia))



  print(_strdato)

  print(type(_strdato))

  print(edato)

  print(type(edato))

  print(ddato)

  print(type(ddato))

  print(dtdato)

  print(type(dtdato))

