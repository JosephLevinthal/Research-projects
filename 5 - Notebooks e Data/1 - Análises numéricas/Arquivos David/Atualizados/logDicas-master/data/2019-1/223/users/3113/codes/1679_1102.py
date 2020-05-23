# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H=float(input("altura total do tanque:"))
h=float(input("nivel de combustivel no tanque:"))
r=float(input("raio dos bojos semiesfericos inferior e superior:"))
print("Entradas:", H, ",", h, ",", r)
if(H>0 and h>0 and r>0 and H>h and H>2*r):
	if(h<r):
		v1=(1/3)*pi*h**2*(3*r-h)
		v=v1*1000
	elif(h<H-r):
		v1=(2/3)*pi*r**3+pi*r**2*(h-r)
		v=v1*1000
	elif(h<=H):
		v1=(4/3)*pi*r**3+pi*r**2*(H-2*r)-(1/3)*pi*(H-h)**2*(3*r-H+h)
		v=v1*1000
	print("Volume:", round(v,3),"litros")
else:
	v="Entradas invalidas"
	print(v)
