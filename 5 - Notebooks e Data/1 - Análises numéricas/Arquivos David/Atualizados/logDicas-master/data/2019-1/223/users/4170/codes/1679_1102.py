# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H = float(input("altura total do tanque: "))
h = float(input("nivel de combustivel no tanque: "))
r = float(input("raio dos bojos semiesfericos: "))
print("Entradas:", H, ",", h, ",", r)
v = (4/6)*pi*(r**3)
vt = (4/3)*pi*(r**3)+pi*(H-2*r)*(r**2)
calota = (pi*((H-h)**2)*((3*r)-(H-h)))/3
if(H>0 and h>0 and r>0 and H>h and H>2*r):
	if(h<r):
		volume = v * 1000
		print("Volume: ", round(volume,3), "litros")
	elif(h>=r and h<H-r):
		volume = (v+(pi*(h-r)*(r**2))) * 1000
		print("Volume: ", round(volume,3), "litros")
	elif(h>=H-r):
		volume = (vt-calota) * 1000
		print("Volume: ", round(volume,3), "litros")
else:
	print("Entradas invalidas")	