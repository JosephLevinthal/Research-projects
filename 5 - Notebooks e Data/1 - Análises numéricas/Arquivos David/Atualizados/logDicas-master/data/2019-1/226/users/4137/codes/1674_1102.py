
from math import*
H = float(input("Altura total do tanque:"))
h = float(input("Nivel de combustivel no tanque:"))
r = float(input("Raio dos bojos semiesfericos infeior e superior:"))

print("Entradas:", H, ",", h, ",", r)

v = (pi/3) * (h**2) * (3*r-h)
v1 = (4*pi*(r**3)/6)+(pi*(r**2)*(h-r))
v2 = ((4*pi*(r**3))/6) + ((pi/3)*((r**2) * (h-r)) *2)

if(H<0 or h<0 or r<0 or H<h or H<2*r):
	print("Entradas invalidas")
elif(h <= r):
		print("Volume: ", round(v * 1000, 3), "litros")
elif(r < h and h <= H-r):
		print("Volume: ", round(v1 * 1000, 3), "litros")
elif(h > H-r):
		print("Volume: ", round(v2 * 1000, 3), "litros")

	