# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H=float(input())
h=float(input())
r=float(input())
Vc=pi*(r**2)*x
Ve=(4*pi*r**3)/3
Vcl=(pi*(x**2)*(3*h-x))/3
if(H>0)and(h>0)and(r>0)and(H>h)and(H>2*r):
	print("Entradas:",H,h,r)
	print("Volume:",Vc+Ve+Vcl,"litros")