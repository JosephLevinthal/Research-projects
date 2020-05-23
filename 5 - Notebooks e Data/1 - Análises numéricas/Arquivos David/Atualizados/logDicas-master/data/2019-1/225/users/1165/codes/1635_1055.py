from math import*

v = float(input("Velocidade inicial: "))
a = radians(float(input("Angulo com o solo: ")))
d = float(input("Distancia do passaro e porco: "))

g = 9.8
R = ((v **2) * sin(2 * a)) / g

if (abs(d - R) <= 0.1):
	msg = "sim"
else:
	msg= "nao"
print(msg)