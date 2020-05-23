from math import*
v = float(input("Velocidade Inicial: "))
a = radians(float(input("angulo com o solo: ")))
D = float(input("distancia entre passaros e porco: "))

g = 9.8
R = ((v**2))*sin((2*a))/g
if (abs(R - D)) <= 0.1:
	print("sim")
else:
	print("nao")