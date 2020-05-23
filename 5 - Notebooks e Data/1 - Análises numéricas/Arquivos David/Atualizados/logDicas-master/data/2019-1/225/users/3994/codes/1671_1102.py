# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
H=float(input("Digite a altura total: "))
h=float(input("Digite o nivel de combustivel: "))
r=float(input("Digite o raio: "))
print("Entradas:",H,",",h,",",r)
from math import*
if(H>0 and h>0 and r>0 and H>h and H>(2*r)):
	if(h==r):
		v=(2/3 * pi * r**3)
		print("Volume: ", round((v*1000),3) ,"litros")
	elif(h<r):
		v=(pi/3)*(h**2)*(3*r-h),3
		print("Volume: ", round((v*1000),3) ,"litros")
	elif(h== H-r):
		v=(((pi*(r**2))*(H - 2*r)) + (2/3) * pi * (r**3))
		print("Volume: ", round((v*1000),3) ,"litros")
	elif(h<H-r and h>r):
		v=(pi*(r**2)*(h - r)) + (2/3 * pi * r**3)
		print("Volume: ", round((v*1000),3) ,"litros")
	else:
		v=((pi*(r**2)*(H - 2*r)) + (4/3 * pi * r**3)) - ((pi/3)*((H-h)**2)*(3*r-(H-h)))
		print("Volume: ", round((v*1000),3) ,"litros")
else:
	print("Entradas invalidas")
		
			
	
	
	

