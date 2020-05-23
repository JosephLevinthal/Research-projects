H=float(input("insira a altura do tanque: "))
h=float(input("insira o nivel de combustivel no tanque: "))
r=float(input("insira o raio dos bojos semiesfericos inferior e superior: "))
from math import*
if ((h>0)and(H>0)and(r>0))and(H>h)and(H>2*r):
	if(h<r):
		vol=(pi/3)*(h**2)*(3*r-h)
		v=round((vol*1000),3)
		print("Entradas:",H,",",h,",", r)
		print("Volume:",v,"litros")
	elif(h<(H-r)):
		vol=(2/3)*pi*(r**3)+pi*(r**2)*(h-r)
		v=round((vol*1000),3)
		print("Entradas:",H,",",h,",", r)
		print("Volume:",v,"litros")
	elif(h<=H):
		vol=(4/3)*pi*(r**3)+pi*(r**2)*(H-2*r)-(pi/3)*((H-h)**2)*(3*r-H+h)
		v=round((vol*1000),3)
		print("Entradas:",H,",",h,",", r)
		print("Volume:",v,"litros")
else:
	print("Entradas:",H,",",h,",", r)
	print("Entradas invalidas")
