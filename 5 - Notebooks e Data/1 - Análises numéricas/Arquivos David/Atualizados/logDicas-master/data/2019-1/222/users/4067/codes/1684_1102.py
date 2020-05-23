# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H = float(input())
h = float(input())
r = float(input())
print("Entradas: ", H,",","h",",", r)
if H > 0 and h > 0 and r > 0 and H > h and H > 2*r:
	#semiesfera inferior
	if r == h:
		print("Volume:",round(pi/3 * r**2 * (3* r - r),3))
	#cilindro
	if H == h:
		print("Volume:",round((pi * r**2 * H) + pi/ 3 * r**2 (3*r - r))
	#semiesfera superior
	if 
	