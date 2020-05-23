import math

v0 = float(input("Velocidade inicial: "))
a = math.radians(float(input("Angulo do vetor de lancamento com o solo: ")))
D = float(input("Distancia horizontal entre o passaro e o porco: "))

R = ((v0 ** 2) * math.sin(2 * a)) / 9.8

if((abs(D - R) >= 0.0) and (abs(D - R) <= 0.1)):
	print("sim")
else:
	print("nao")