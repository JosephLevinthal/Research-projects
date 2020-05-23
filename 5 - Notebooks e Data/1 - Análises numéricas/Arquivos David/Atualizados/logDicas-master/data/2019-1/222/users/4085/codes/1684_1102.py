# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
H = float(input("escreva o valor da altura total: "))
h = float(input("escreva o valor da altura do combustivel: "))
r = float(input("escreva o valor do raio: "))
print ("Entradas:", H,",", h,",", r)
if (H < 0) or (h < 0) or (r < 0) or (H < h) or (H < 2 * r):
	print ("Entradas invalidas")
else: 
	if (h < r):
		V = (1/3) * pi * (h ** 2) * (3 * r - h)
	elif (h < H - r):
		V = (2/3) * pi * r ** 3 + pi * r ** 2 * (h - r)
	elif (h <= H):
		V = (4/3) * pi * (r ** 3) + pi * (r ** 2) * (H - 2 * r)- (1/3) * pi * ((H - h) ** 2) * (3 * r - (H - h))
	print ("Volume:", round(V * 1000, 3),"litros")