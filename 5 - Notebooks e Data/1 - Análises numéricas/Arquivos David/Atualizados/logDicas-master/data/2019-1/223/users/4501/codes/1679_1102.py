# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
from math import*
H=float(input("altura do tanque: "))
h=float(input("nivel de combustivel: "))
r=float(input("raio dos bojos: "))
print("Entradas: ",H, "," ,h ,"," ,r)

if(H>0 and h>0 and r>0)and(H>h and H>(2*r)):
	V=(4/3)*pi*(r**3)
	if(h <= r):
		if(h==r):
			v=(V/2)*1000
			print("Volume: ",round(v, 3),"litros")
		elif(h<r):
			v=((pi/3)*(h**2)*(3*r-h))*1000
			print("Volume: ",round(v, 3)<"litros")
	elif(h>r and h<=H-r):
		v=V/2
		C=pi*(r**2)*(h-r)
		v1=(v+C)*1000
		print("Volume: ",round(v1, 3),"litros")
elif(H<0 or h<0 or r<0)or(H<h or h<2*r):
	print("Entradas invalidas")
	