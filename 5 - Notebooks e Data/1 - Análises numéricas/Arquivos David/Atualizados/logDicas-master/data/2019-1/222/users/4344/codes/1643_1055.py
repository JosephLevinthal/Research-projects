import math as m
g = 9.8
vo = float(input("valeocidade inicial: "))
a  = float(input("angulo do vetor de lancamento com solo: "))
D  = float(input("Distancia entre o bird and pig: "))

R = ((vo**2)*m.sin(m.radians(2*a)))/g

if abs(D - R) <= 0.1:
	print("sim")
else:
	print("nao")