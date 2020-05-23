raio=float(input("raio"))
altura=float(input("altura"))
num=int(input("num"))
from math import*
vol=((4*pi)*(raio**3))/3
volar=(pi*(altura**2)*(3*raio-altura))/3
volcomb=vol-volar
if(num==1):
	print(round(volar,4))
else:
	print(round(volcomb,4))
	
