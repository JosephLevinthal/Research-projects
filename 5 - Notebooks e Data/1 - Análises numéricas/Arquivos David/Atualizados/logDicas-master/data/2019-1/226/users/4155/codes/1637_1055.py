from math import *
vo = float(input("velocidade inicial: "))
a = float(input("angulo: "))
d = float(input("distancia: "))
g = 9.8
R = (((vo) ** 2) * sin(radians(2 * a))) / g
x = abs(d - R)

if (x <= 0.1):
	msg = "sim"
else:
	msg = "nao"
print(msg)

