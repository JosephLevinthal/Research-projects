from math import *

H = float(input("Altura total do tanque (H): "))
h = float(input("Nivel do combustivel no tanque (h): "))
r = float(input("Raio dos bojos semiesfericos inferior e superior (r): "))

esf = ((4/3) * pi * (r**3))
cal = ((pi / 3) * (r**2) * (3*r - h))
cil = (pi * (r**2) * (h-r))

if H > 0 and h > 0 and r > 0 and H > h and H > (2 * r):
	if (h < r):
		V = cal
	
	elif (h < H - r):
		V = (esf/2) + cil
		
	
	elif (h <= H):
		cal = (pi/3) * (H-h)**2 * (3 * r - H+h)
		cil = pi * r **2 * (H-2*r)
		V = esf + cil - cal
	
	V *= 1000
	V = round(V,3)	
	print("Entradas:", H,",",h,",",r)
	print("Volume: ", V, "litros")

else:
	print("Entradas:", H,",",h,",",r)
	print("Entradas invalidas")