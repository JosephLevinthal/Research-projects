H = float(input("Valor: "))
h = float(input("Valor: "))
r = float(input("Valor: "))

print("Entradas:", H, ",", h, ",", r)

from math import *

if (H > 0) and (h > 0) and (r > 0) and (H > h) and (H > 2*r):
	if (h <= r):
		v = (pi/3) * (h ** 2) * (3 * r - h)
		print("Volume: ", round(v * 1000, 3), "litros")
	elif (r < h) and (h <= H - r):
		v = (4 * pi * (r ** 3) / 6) + (pi * (r ** 2) * (h - r))
		print("Volume: ", round(v * 1000, 3), "litros")
	elif (h > H - r):
		v = ((4 * pi * (r ** 3))/ 6 ) + ((pi/3) * ((r ** 2) * (h - r)) * 2)
		print("Volume: ", round(v * 1000, 3), "litros")
else:
	print("Entradas invalidas")
		