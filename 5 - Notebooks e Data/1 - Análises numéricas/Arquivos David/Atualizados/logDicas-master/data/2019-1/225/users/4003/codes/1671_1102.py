# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*
H = float(input("digite altura: "))
h = float(input("digite o raio: "))
r = float(input("digite o nivel de combustivel: ")) 
print("Entradas:", H, ",",h,",",r)

if ( h < 0 and H < 0 and r < 0 and h > H and H > 2 * r):
	if ( h == r ):
		v = ((4/3) * pi * (r**3))/2
		print("V:",(round((v*1000),3)),"litros")
	elif( h < r):
		v = (pi/3) * (h**2) * (3*r-h)
		print("V:",(vol*1000), "litros")
	elif( h == H - r ):
		v = round(((pi * (r**2) * (H-2*r)) + (2/3) * pi * (r**3)),3)
		print("V:",(v*1000),"litros")
	elif( h < H - r and h > r):
		v = pi * (r**2) * (h - r) + ((4/3) * pi * (r**3))/2
		print("V:",(round((v*1000),3)),"litros")
	else:
		v = pi * (r**2) * (H-2*r) + 4/3 * pi * (r**3) - (pi/3) * ((H-h)**2) * (3 * r - (H-h))
		print("V:",(round((v*1000),3)),"litros")
		
else:
	print("Entradas invalidas")