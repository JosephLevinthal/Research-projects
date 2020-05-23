from math import*

v0 = float(input("velicidade inicial:"))
a = radians(float(input("angulo do vetor:")))
D = float(input("distancia entre o passaro e o porco:"))
g = 9.8

R = ((v0**2) * (sin(2*a))) / g

tolerancia = abs(D - R)

if(tolerancia <= 0.1):
	print("sim".lower())
else:
	print("nao".lower())
