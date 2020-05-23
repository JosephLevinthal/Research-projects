# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

ht = float(input("altura total do tanque:"))
h = float(input("nivel de combustivel no tanque:"))
r = float(input("raio:"))

print("Entradas: ", ht,",", h,",", r)

v = (4/6)*pi*(r**3)
vt = (4/3)*pi*(r**3) + pi*(ht - 2*r)*(r**2)
calota = (pi*((ht - h)**2)*((3*r)-(ht - h)))/3

if (ht > 0) and (h > 0) and (r > 0) and (ht > h) and (ht > (2*r)):
	if ( h < r):
		vol = v*1000
		print("Volume:",round(vol,3),"litros")
	elif ( h >= r) and (h < (ht - r)):
		vol = (v + (pi*(h - r)*(r**2)))*1000
		print("Volume:",round(vol,3),"litros")
	elif (h >= (ht - r)):
		vol = (vt - calota)*1000
		print("Volume:",round(vol,3),"litros")
else:
	print("Entradas invalidas")
