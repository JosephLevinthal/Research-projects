# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
H= float(input(""))
nc = float(input(""))
rb = float(input(""))
print("Entradas: ", H,",", nc,",", rb)
if(H>0 and nc>0 and rb>0 and H>nc and H>2*rb):
	if(nc<=rb):
		v=(pi/3) * (nc**2) * (3*rb - nc)
		print("Volume: ", round(v*1000,3), "litros")
	elif(rb<nc and nc<= H-rb):
		v = (4*pi*(rb**3)/6) + (pi*(rb**2)*(nc-rb))
		print("Volume: ", round(v*1000,3), "litros")
	elif(nc>H-rb):
		v= ((4*pi*(rb**3)/6 + (pi/3)* (rb**2)* (nc - rb))*2)
		print("Volume: ", round(v*1000,3), "litros")
else:
	print("Entradas invalidas")
		
		