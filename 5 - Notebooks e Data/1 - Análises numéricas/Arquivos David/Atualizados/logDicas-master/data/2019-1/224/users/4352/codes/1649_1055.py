# velocidade inicial em m/s = v0
v0 = float(input("digite a velocidade inicial: "))
# angulo alfa em graus
a = float(input("digite o angulo alfa: "))
# distancia horizontal D em metros
d = float(input("digite a distancia: "))
#gravidade
g = 9.8
##########################################
from math import *
r = (v0)**2 * sin(radians(2 * a)) / g 

if abs(d - r) < 0.1:
	print("sim")
else:
	print("nao")