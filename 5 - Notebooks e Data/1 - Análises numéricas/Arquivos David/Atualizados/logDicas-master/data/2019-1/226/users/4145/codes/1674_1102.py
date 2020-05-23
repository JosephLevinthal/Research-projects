from math import*
H = float(input("altura do tanque: "))
h = float(input("nivel de combustivel: "))
r = float(input("raio dos bojos: "))
print("Entradas:",H," , ",h," , ",r)
ve =4/3*pi*r**3
vc =(pi*r**2)+(H-2*r)

if((H>h)and(H>2*r)and(h>0)and(H>0)and(r>0)):
	if(h<=r):
		v = ((pi/3)*(h**2)*(3*r-h))
	elif(h>r and h<= H - r):
		v = 1/2*ve + pi*(r**2)*(h-r)
	
	elif(h >H-r):
		v = ve +  vc -((pi/3)*(r**2)*(h-r))*2
	print("Volume:",round(v*1000,3),"litros")	
else:
	print("Entradas invalidas")