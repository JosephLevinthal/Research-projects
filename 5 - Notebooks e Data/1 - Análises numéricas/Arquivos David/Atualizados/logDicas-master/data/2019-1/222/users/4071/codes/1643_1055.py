from math import*
a=float(input("velocidade inicial:"))
b=radians(float(input("angulo:")))
d=float(input("distancia:"))

r=(a**2)*sin(2*b)/9.8

p= d-r
if(abs(p)<0.1):
	print("sim")
else:
	print("nao")