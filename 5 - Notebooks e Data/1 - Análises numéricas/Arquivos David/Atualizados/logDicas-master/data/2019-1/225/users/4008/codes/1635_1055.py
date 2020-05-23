from math import*
vo = float(input("velocidade incial: "))
alpha = radians(float(input("angulo em graus: ")))
d = float(input("distancia entre o porco e o passaro: "))
r = (vo**2 * sin(2*alpha)) / 9.8
if abs(d - r) <= 0.1:
	print("sim")
else:
	print("nao")