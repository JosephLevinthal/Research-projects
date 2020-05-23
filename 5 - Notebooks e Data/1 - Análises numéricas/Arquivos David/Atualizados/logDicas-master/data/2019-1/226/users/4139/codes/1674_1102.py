from math import *
H = float(input("altura do tanque:"))
h = float(input("nivel do tanque:"))
r = float(input("raio do tanque:"))

a = "Volume:"
b = "litros"

print("Entradas:",H,",",h,",",r)

if(H>0)and(h>0)and(r>0):
	if(H>h)and(H>2*r):
		if(h<=r):
			v=(pi/3)*(h**2)*(3*r-h)
			print(a,round(v*1000,3),b)
		elif(h>r) and (h<=H-r):
			x = (4*pi*(r**3))/6
			y = pi*(r**2)*(h-r)
			v = x+y
			print(a,round(v*1000,3),b)
		elif(h>H-r):
			x = (4*pi*(r**3))/6
			y = pi*(r**2)*(a-2*r)
			z = x - ((pi*((a-h)**2)*(3*r-(a-h)))/3)
			v = x+y+z
			print(a,round(v*1000,3),b)
	else:
		print("Entradas invalidas")
else:
	print("Entradas invalidas")
