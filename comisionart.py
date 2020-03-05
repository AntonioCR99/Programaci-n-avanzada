import re

def comision(valor):
  valorfijo=300
  valorvariable=valor*0.20
  if valor >= 1000:
    return valorfijo
  else:
    return valorvariable

_aportacion=""
aportacion=0.00
minimo=500
while True:
  _aportacion = input("Aportacion: ")
  if re.search("^\d+(\.\d+)?$",_aportacion):
    aportacion = float(_aportacion)
    if aportacion <minimo:
      print("Aportacion minima $500.00")
    else:
      break
  else:
    print("Se requiere una cantidad")

txt="Aportacion al artista ${:,.2f}"
print(txt.format(comision(aportacion)))