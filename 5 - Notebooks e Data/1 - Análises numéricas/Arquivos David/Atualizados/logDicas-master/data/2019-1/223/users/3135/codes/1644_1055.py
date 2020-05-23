from math import*
v=float(input("Insira a velocidade inicial:"))
a=radians(float(input("Insira o angulo(em graus):")))
D=float(input("Insira a distancia entre P/P:"))

g= 9.8
R=((v)**2) * sin(2*a) / g
T= abs(D-R)

if (T <= 0.1):
	print("sim")
else:
	print("nao")