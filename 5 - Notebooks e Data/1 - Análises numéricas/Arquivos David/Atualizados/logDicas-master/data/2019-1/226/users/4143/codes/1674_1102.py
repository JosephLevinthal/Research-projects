from math import*
a = float(input("altura tanque:"))
h = float(input("nivel de combustivel no tanque:"))
r =float(input("raio dos bojos semi esfericos inferior e superior:"))
print("Entradas: ", a,",", h,",", r)
if (h<0)or(a<=0)or(r<=0):
	print("Entradas invalidas")
elif (h>a) or (2*r>a):
	print("Entradas invalidas")
else:
	if (h<=r):
		v = (pi/3)*(h**2)*(3*r - h)
		print("Volume: ", round(v*1000,3), "litros")
	elif (h>r) and (h<=a-r):
		v2= (4*pi*(r**3))/6
		v3= pi*(r**2)*(h-r)		
		v = v2 + v3
		print("Volume: ", round(v*1000,3), "litros")
	elif (h>a-r):
		v2 = (4*pi*(r**3))/6
		v3 = pi*(r**2)*(a-2*r)		
		v4 = v2 - ((pi*((a-h)**2)*(3*r-(a-h)))/3)
		v = v2 + v3 + v4
		print("Volume : ", round(v*1000, 3), "litros")