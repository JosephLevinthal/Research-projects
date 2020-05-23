from math import*
v0 = float(input("velocidade inial:"))
a  = radians(float(input("angulo do vetor:")))
d = float(input("distancia:"))

g = 9.8
R = ((v0**2) *sin(2*a))/g
if (abs(R- d) <= 0.1):
	 print("sim")
else:
	 print("nao")
	