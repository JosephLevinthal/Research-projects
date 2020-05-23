from math import*
v0 = float(input("Velocidade inicial:"))
a = float(input("Angulo:"))
d = float(input("Distancia do porco horizontalmente:"))
g= 9.8
ang = radians(a)
R = (((v0)**2)*sin(2*ang))/g
x = abs(d-R)
if (x<=0.1):
	print("sim")
else:
	print("nao")
