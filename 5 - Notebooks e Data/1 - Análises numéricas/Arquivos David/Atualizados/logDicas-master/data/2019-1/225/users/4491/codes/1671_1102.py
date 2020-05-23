# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H = float(input("altura total: "))
h = float(input("nivel de combustivel: "))
r = float(input("raio de bojos: "))
from math import *
Vc = pi*(r**2)*x
ve = 4/3*pi*(r**3)
Vca = pi/3*(x**2)*(3*r - x)
print("Entradas:", H,",", h,",",r)

if(H > 0) and (h > 0) and (r > 0):
	if(H > h) and (H > z):
		print("Volume:", round(Vc,2),"litros")
	