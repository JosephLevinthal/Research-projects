x = float(input("valor de x: "))

from math import *

if(-1 <= x < - 1/2) or (1/2 < x <= 1):
	f = asin(x)
	print(round(round(f, 2)))
elif(-1/2 <= x <= 1/2):
	g = acos(x)
	print(degrees(round(g, 2)))
else: 
	print("entrada invalida")