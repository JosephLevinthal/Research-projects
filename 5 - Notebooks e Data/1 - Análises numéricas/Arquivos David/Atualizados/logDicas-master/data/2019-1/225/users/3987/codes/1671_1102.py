# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H = float(input("altura:"))
h = float(input("nivel:"))
r = float(input("raio:"))
from math import *
print("Entradas:", H, ",", h, ",", r,)
if(H > 0) and (h > 0) and (r > 0) and (H > h) and (H > 2*r):
	if(h == r):
		vol = round(((4/3)* pi * (r**3))/2,3)
		print("Volume:",(vol*1000), "litros")
	elif(h < r):
		vol = round(((pi*(r**2)*(H-2*r))+(2/3)*pi*(r**3)),3)
		print("Volume:", (vol*1000), "litros")
	elif(h < H - r) and (h > r):
		vol = round((pi*(r**2)*(h-r)+(4/3)*pi*(r**3))/2,3)
		print("Volume:", (vol*1000), "litros")
	else:
		vol = round((pi*(r**2)*(H-2*r)+4/3*pi*(r**3)-(pi/3)*(H-h)**2)*(3*r-(H-h)),3)
		print("Volume:", (vol*1000), "litros")
else:
	print("Entradas invalidas")
		
		
		
		