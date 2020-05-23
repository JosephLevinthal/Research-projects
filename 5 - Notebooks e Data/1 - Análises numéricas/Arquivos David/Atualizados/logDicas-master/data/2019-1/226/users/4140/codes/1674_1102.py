H=float(input())
h=float(input())
r=float(input())
from math import*
print("Entradas:",H,",",h,",", r)
if(H<=0 or h<=0 or r<=0 or H<h or H<h or H<2*r):
	print("Entradas invalidas")
else:
	if(H==h):
		v= ((4/3)*pi*r**3 + ((H-2*r)*pi*r**2))*1000
		print("Volume:",round(v,3) ,"litros")
	elif(h>r and h<H and h>(r+(H-2*r))):
		v= (((4/3)*pi*r**3)/2 + pi*r**2*(H-2*r) +(((4*pi/3)*r**3)/2) -((pi/3)*(H-h)**2)*(3*r-(H-h)))*1000
		print("Volume:",round(v,3) ,"litros")
	elif(h>r and h<H and h==H-r):
		v=(((4/3)*pi*r**3)/2 +pi*r**2*(H-2*r))*1000
		print("Volume:",round(v,3) ,"litros")
	elif(h>r and h<H and h<(H-r)):
		v=(((4/3)*pi*r**3)/2+ pi*r**2*(h-r))*1000
		print("Volume:",round(v,3) ,"litros")
	elif(h==r):
		v=(((4/3)*pi*r**3)/2)*1000
		print("Volume:",round(v,3) ,"litros")
	elif(h<r):
		v=((pi/3)*h**2*(3*r-h))*1000
		print("Volume:",round(v,3) ,"litros")
			

		 
	
	