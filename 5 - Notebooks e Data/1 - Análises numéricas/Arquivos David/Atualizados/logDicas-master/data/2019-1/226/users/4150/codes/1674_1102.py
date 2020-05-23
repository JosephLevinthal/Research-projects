from math import*

H = float(input("altura do tanque: "))
h = float(input("nivel de combustivel no tanque: "))
r = float(input("raio: "))

print("Entradas:", H ,",", h, ",", r )

vc = ((pi)*(r**2)*(H)
ve = (4/3)*(pi)*(r**3)
vca = ((pi/3)*(H**2))*(3*r - H)

if (H<0) or (h<0) or (r<0) :
	print("Entradas invalidas")
else:
	if (H<h) and (H<(2*r)):
		print("Entradas invalidas")
	else:
		if(H>h):
			print("Volume:" )