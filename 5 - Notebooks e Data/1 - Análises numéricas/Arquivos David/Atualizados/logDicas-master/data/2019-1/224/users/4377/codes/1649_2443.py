raio=float(input("raio"))
altura=float(input("h"))
nu=int(input("nu"))

#1  volume de ar=calota #2 volume combustivel= vt-calota
from math import*
total=( (4*pi) * (raio**3) ) /3
calota= ( ( (pi) * (altura**2) ) * ( (3*raio) - (altura) ) ) /3
comb=total-calota

if(nu==1):
	print(round(calota,4))
if(nu==2):
	print(round(comb,4))