from math import*
v=float(input("v inicial:   "))
a=float(input("angulo:   "))
d=float(input("distancia:   "))
r=((v**2)*(sin(2*(radians(a)))))/9.8
r=abs(r)
if(d-r)<0.1:
	print("sim")
else:
	print("nao")