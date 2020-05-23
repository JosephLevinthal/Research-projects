# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H=float(input("altura do tanque: "))
c=float(input("nivel do combustivel: "))
r=float(input("raio semiesferico: "))
print("Entradas:",H,",",c,",",r)
from math import *
if(H>0 and c>0 and r>0)and(H>c and H>(2*r)):
	V=(4/3)*pi*(r**3)
	if(c<=r):
		if(c==r):
			v=(V/2)*1000
			print("Volume:",round(v,3),"litros")
		elif(c<r):
			v=((pi/3)*(c**2)*(3*r-c))*1000
			print("Volume:",round(v,3),"litros")
	elif(c>r and c<=H-r):
		v=V/2
		C=pi*(r**2)*(c-r)
		V1=(v+C)*1000
		print("Volume:",round(V1,3),"litros")
	elif(c>H-r):
		C=pi*(r**2)*(c-r)
		vc=(pi/3)*((H-c)**2)*(3*r-(H-c))
		V1=((V/2)+C-vc)*1000
		print("Volume:",round(V1,3),"litros")
elif(H<0 or c<0 or r<0) or (H<c or c<2*r):
	print("Entradas invalidas")