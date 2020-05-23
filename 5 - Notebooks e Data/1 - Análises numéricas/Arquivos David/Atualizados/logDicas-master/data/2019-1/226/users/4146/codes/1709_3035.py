from math import *

x1 = float(input("Valor de x: "))

x = radians(x1)

if (0 <= x1 < 360):
	if (0 <= x1 < 90) or (180 <= x1 < 270):
		y = sin(x)
		print(round(y, 4))
	elif (90 <= x1 < 180) or (270 <= x1 < 360):
		y = cos(x)
		print(round(y, 4))
else:
	print("entrada invalida")