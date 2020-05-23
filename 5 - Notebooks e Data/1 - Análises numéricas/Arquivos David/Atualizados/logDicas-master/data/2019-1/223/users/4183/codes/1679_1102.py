H = float(input("Altura total do tanque: "))
h = float(input("Nivel de combustivel no tanque: "))
r = float(input("Raio dos bojos: "))
print("Entradas: ", H, ",", h, ",", r)

from math import *
 
if(H < 0 or h < 0 or r < 0) or (H < h or h < 2*r):
	print("Entradas invalidas")
else:
	V = (4/3)*pi*(r**3)
	if (h == r):
		v = (V/2)*1000
		print("Volume: ", round(v,3), "litros")
	elif (h<r):
		v = ((pi/3)*(h**2)*(3*r-h))*1000
		print("Volume: ", round(v,3), "litros")
	elif (h>r and h<=H-r):
		v = V/2	
		C = pi*(r**2)*(h-r)
		V1 = (v+C)*1000
		print("Volume", round(V1,3), "litros")
	elif (h > H-r):
		C = pi*(r**2)*(h-r)
		vc = (pi/3)*((H-h)**2)*(3*r - (H-h))
		V1 = ((V/2) + C - vc)*1000
		print("Volume:", round(V,3), "litros")







