from math import*
v0= float(input("velocidade: "))
a= radians(float(input("angulo: ")))
g=9.8
D =(float((input"distancia: "))
R = (v0**2)*(sin(2*a))/2
if(D<=R):
	msg = "sim"
else:
	msg = "nao"
print(msg)
