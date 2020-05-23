# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H=float(input("Diga a altura total do tanque: "))
h=float(input("Diga o nivel de combustivel no tanque: "))
r=float(input("Diga o raio dos bojos semiesfericos inferior e superior: "))
print("Entradas:", H, ",", h, ",", r)
if (H>0) and (h>0) and (r>0) and (H>h) and (H>2*r):
	Vc=(pi*r**2*H)+2*(pi/3*r**2*(3*r-r))-(pi*r**2*h)
	print("Volume:", round(Vc, 3), "litros")
else:
	print("Entradas invalidas")