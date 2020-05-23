# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

H = float(input("Insira a altura total do tanque: "))
h = float(input("Insira o nivel de combustivel: "))
r = float(input("Insira o raio dos bojos: "))

print("Entradas:", H,",", h,",", r)

if((H > 0) and (h > 0) and (r > 0) and (H > h) and (H > 2*r)):
	if(h <= r):
		v = (pi/3)*(h ** 2)*(3 * r - h)
		print("Volume: ",round(v * 1000,3), "litros")
	elif(r < h and h <= H -r):
		v = (4 * pi * (r ** 3)/ 6) + (pi * (r ** 2) * (h - r))
		print("Volume: ",round(v * 1000,3), "litros")
	elif(h > H - r):
		v = ((4 * pi * (r ** 3))/ 6) + ((pi/3) * ((r ** 2) * (h - r) * 2))
		print("Volume: ",round(v * 1000,3), "litros")
else:
	print("Entradas invalidas")