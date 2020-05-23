from math import *

Vo = float(input("digite Vo: "))
alpha = radians(float(input("digite alpha: ")))
d = float(input("digite distancia: "))

g = 9.8
R = (Vo ** 2 * sin (2 * alpha)) / g 

if (abs(d - R) < 0.1):
	 print("sim")
else:
	 print("nao")
