from math import*
a = float(input("altura do tanque: "))
h = float(input("nivel de combustivel do tanque: "))
r = float(input("raio dos bojos semiesfericos inferior e superior: "))
print("Entradas: ",a,",",h, ",",r)
if(h<0) or(a<=0) or (r<=0):
	print("Entradas invalidas")
elif(h>a)or (2*r>a):
	print("Entradas invalidas")
else:
	if(h<=r):
		v = (pi/3)*(h**2)*(3*r - h)
		print("Volume: ", round(v*1000,3),"litros")
	elif(h>r) and(h<=a-r):
		vse = (4*pi*(r**3))/6
		vc = pi*(r**2)*(h-r)
		v = vse + vc
		print("Volume: ", round(v*1000,3),"litros")
	elif(h>a-r):
		vse = (4*pi*(r**3))/6
		ve = vse - ((pi*((a-h)**2)*(3*r-(a-h)))/3)
		v = vse + vc + ve
		print("Volume: ", round(v*1000,3),"litros")
		