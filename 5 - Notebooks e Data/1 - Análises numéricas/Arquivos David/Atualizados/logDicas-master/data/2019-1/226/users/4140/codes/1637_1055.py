vo=float(input())
angulo=float(input())
g=9.8
distancia=float(input())

from math import *
angulo1= radians(angulo);
from math import *
horizontal=((vo**2)*sin(2*angulo1))/g

if(abs(distancia-horizontal)<=0.1):
	print("sim")
else:
	print("nao")