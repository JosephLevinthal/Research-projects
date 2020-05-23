h1=float(input(" altura total: "))
h2=float(input("nivel de combustivel no taque: "))
r=float(input("raio dos bojos semiesfericos inferior e superior: "))
print("Entradas: ",h1,"," , h2,",", r)
from math import*
if(h1>0 and h2>0 and r>0 and h1>h2 and h1>2*r):
	if(h2<=r):
		v=(pi/3)*(h**2)*(3*r-h)
		print("Volume: ",round(v*1000,3),"litros")
	elif(r<h2 and h2<=h1-r):
		#v=(pi*(r**2)*h2)+((pi/3)*(h2**2)*(3*r-h2))
		v=(4*pi*(r**3)/6)+(pi*(r**2)*(h2-r))
		print("Volume: ",round(v*1000,3),"litros")
	elif(h2>h1-r):
		v=(4*pi*(r**3)/6)+((pi/3)*((r**2)*(h2-r))*2)
		print("Volume: ",round(v*1000,3),"litros")
else:
	print("Entradas invalidas")
