from math import *

v = float(input("Velocidade inicial: "))
a = radians(float(input("Angulo co o solo: ")))
D = float(input("Distancia entre passaro e porco: "))
g = 9.8

R = ((v ** 2) * sin(2 * a)) / g

if (abs(R - D) <=0.1):
	print ("sim")
else:
	print ("nao")