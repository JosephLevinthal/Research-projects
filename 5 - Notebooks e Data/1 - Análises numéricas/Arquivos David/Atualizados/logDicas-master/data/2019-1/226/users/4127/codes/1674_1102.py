from math import*
a= float(input("qual a altura total do tanque? "))
h= float(input("qual o nivel de combustivel no tanque? "))
r= float(input("qual o raio dos bojos? "))
print("Entradas:", a,",", h,",", r)

if(h<0) or (a<=0) or (r<=0):
	print("Entradas invalidas")
elif (h>a) or (h<2*r):
	print("Entradas invalidas")
else:
	if (h<=r):
		v= (pi/3)*(h**2)*(3*r-h)
		print("Volume:", round(v*1000,3), "litros")
	elif (h>r) and (h<=a-r):
		vse=(4*pi*(r**3))/6
		vc= pi*(r**2)*(h-r)
		v= vse+vc
		print("Volume: ", round(v*1000, 3), "litros")
	elif(h>a-r):
		vse= (4*pi*(r**3))/6
		vc= pi*(r**2)*(a-2*r)
		ve= vse -((pi*((a-h)**2)*(3*r-(a-h)))/3)
		v= vse + vc + ve
		print("Volume: ", round(v*1000,3), "litros")
		
	