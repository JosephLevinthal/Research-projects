from math import*
vo= float(input('Velocidade inicial(m)'))
a= radians(float(input("angulo")))
D= abs(float(input("distancia")))
g = 9.8
R= ((vo)**2*sin(2*a)/g)
if(D-R < 0.1):
	print("sim")
else:
	print("nao")