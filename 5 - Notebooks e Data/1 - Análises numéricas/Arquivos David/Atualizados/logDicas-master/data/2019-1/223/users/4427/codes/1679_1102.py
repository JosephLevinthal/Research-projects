# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*
H=float(input("Qual a altura do tanque (m)?: "))
h=float(input("Qual o nivel do combustivel (m**3)?:"))
r=float(input("Qual o raio (m)?: "))

print("Entradas:", H, ",", h, ",", r)

if (H>0 and h>0 and r>0 and H>h and H>2*r):
	if(h<r):
		V1=(1/3)*pi*h**2*(3*r-h)
		Vol=V1*1000
		print("Volume:",round(Vol,3),"litros")
	elif (h<H-r):
		V1=(2/3)*pi*r**3+pi*r**2*(h-r)
		Vol=V1*1000
		print("Volume:",round(Vol,3),"litros")
	elif (h<=H):
		V1=(4/3)*pi*r**3+pi*r**2*(H-2*r)-(1/3)*pi*(H-h)**2*(3*r-H+h)
		Vol=V1*1000
		print("Volume:",round(Vol,3),"litros")
else:
	Vol="Entradas invalidas"
	print(Vol)




