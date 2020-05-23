r = float(input("digite o raio: "))
x = float(input("digite a altura: "))
v = int(input("volume? (1/2): "))

from math import *

if (v == 1):
	v = (pi * x ** 2 * (3 * r - x)) / 3 
else:
	v = ((4 * pi * r ** 3) / 3) - ((pi * x ** 2 * (3 * r - x)) / 3 )
	
print(round(v, 4))
	



