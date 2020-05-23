from math import*
v0= float(input("velocidade inicial"))
a=radians(float(input("angulo em graus")))
D=float(input("distancia horizontal"))
g=9.8
R= ((v0**2)*(sin(2*a)))/g

if (abs(D-R)<0.1):
	print("sim")
else:
	print("nao")
