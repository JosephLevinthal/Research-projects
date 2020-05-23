# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
H = float(input("Digite a altura: "))
h = float(input("Digite o raio: "))
r = float(input("Digite o volume: "))
print("Entradas:", H, ",", h, ",", r)

if((H>0)and(h>0)and(r>0)and(H>h)and(H>2*r)):
	if(h==r):
		vol= ((4/3)*pi*(r**3))/2
		print("Volume:",(round((vol*1000), 3)),"litros")
	elif(h<r):
		vol= (pi/3)*(h**2)*(3*r-h)
		print("Volume:",(round((vol*1000), 3)),"litros")
	elif(h==H-r):
		vol= (pi*(r**2)*(H-2*r)+(2/3)*pi*(r**3))
		print("Volume:",(round((vol*1000), 3)),"litros")
	elif(h<H-r and h>r):
		vol= pi*(r**2)*(h-r)+((4/3)*pi*(r**3))/2
		print("Volume:",(round((vol*1000), 3)),"litros")
	else:
		vol= pi*(r**2)*(H-2*r)+ 4/3*pi*(r**3)-(pi/3)*((H-h)**2)*(3*r-(H-h))
		print("Volume:",(round((vol*1000), 3)),"litros")
else:
	print("Entradas invalidas")
