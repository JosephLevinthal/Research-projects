
from math import*
g = 9.8
v0 = float(input("vel. inicial: "))
a = float(input("Graus: "))
d = float(input("distancia: "))

if abs(sin(radians(2*a))/g*v0**2 - d) > 0.1:
	print('nao')
else:
	print('sim')