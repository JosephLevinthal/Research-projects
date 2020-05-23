from math import*

V= float(input("velocidade inicial: "))

ANG= radians(float(input("angulo: ")))

D=float(input("distancia: "))

g = 9.8

R= (V) ** 2 * sin( 2  * ANG )  / g

t= abs(D-R)


if (t<0.1):
	men="sim"
else:
	men="nao"
	
print(men)
	
			


