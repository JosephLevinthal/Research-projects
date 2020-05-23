v0= float(input("insira a velocidade inicial: "))
an= float(input("insira o angulo: "))
d= float(input("insira a distancia entre o porco e o passaro: "))
from math import *
r=((v0**2)*sin(radians(2*an)))/9.8
if abs(d-r)<=0.1:
	print("sim")
else:
	print("nao")
