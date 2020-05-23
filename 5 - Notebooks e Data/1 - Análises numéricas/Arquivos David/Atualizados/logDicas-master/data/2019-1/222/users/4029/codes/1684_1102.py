from math import *

H = float(input("Altura total do tanque: "))
h = float(input("Nivel de combustivel do tanque: "))
r = float(input("Raio dos bojos semiesfericos: "))

print("Entradas ", H, ",", h, ",", r)

if (H > 0) and (h > 0) and (r > 0) and (H > h) and (H > (2*r)):
	if (h <= r):
		vol = (pi/3) * (h**2) * (3*r - h)
	if (h > r) and (h <= (H - r)):
		vol = (4/3) * pi * (r**3)
		vol = (vol/2) + (pi * (r**2) * (h - r))
	if (h > r) and (h > (H - r)):
		vol = (4/3) * pi * (r**3)
		vol = vol + (pi * (r**2) * (H - 2*r))
		vol = vol - ((pi/3) * (H - h)**2 * (3*r - (H - h)))
	vol = round(vol*1000, 3)
	print("Volume:", vol, "litros")
else:
	print("Entradas invalidas")