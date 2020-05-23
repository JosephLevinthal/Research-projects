from math import *
v = float(input( "velocidade inicial v0 (em m/s). "))
α =(float(input(" angulo(em graus). ")))
D = float(input("distancia horizontal D(em metros) entre o passaro e o porco. "))
r = (radians(α))
numerador = (v ** 2) * (sin(r * 2))
g = 9.8
R = (numerador /g)
if abs(D - R) < 0.1:
	print("sim")
else : 
	print("nao")