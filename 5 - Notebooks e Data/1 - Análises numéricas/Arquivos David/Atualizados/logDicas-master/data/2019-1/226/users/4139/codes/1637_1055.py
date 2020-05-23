from math import *
vi = float(input("velocidade inicial:"))
a = radians(float(input("angulo em graus:")))
d = abs(float(input("distancia horizontal:")))
g = 9.8

r =((vi)**2)*(sin(2*a))/g

if(abs(d-r) <= 0.1):
	print("sim")
else:
	print("nao")