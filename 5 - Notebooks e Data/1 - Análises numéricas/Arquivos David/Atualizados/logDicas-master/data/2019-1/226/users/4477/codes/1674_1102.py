from math import*
H = float(input("altura do tanque: "))
h = float(input("nivel de combustivel: "))
r = float(input("raio dos bojos: "))

print("Entradas: ", H,",", h,",", r)

if (h<0)or(H<=0)or(r<=0):
	print("Entradas invalidas")
elif (h>H)or(2*r>H):
	print("Entradas invalidas")
else:
	if (h<=r):
		v = (pi/3)*(h**2)*(3*r-h)
		print("Volume: ", round(v*1000, 3), "litros")
	elif (h>r) and (h<=H-r):
		v2 = (4*pi*(r**3))/6
		v3 = pi*(r**2)*(h-r)
		v = v2+v3
		print("Volume: ", round(v*1000, 3), "litros")
	elif (h>H-r):
		v2 = (4*pi*(r**3))/6
		v3 = pi*(r**2)*(a-2*r)
		v4 = v2 - ((pi*((H-h)**2)*(3*r-(H-h)))/3)
		v = v2+v3+v4
		print("Volume: ", round(v*1000, 3), "litros")