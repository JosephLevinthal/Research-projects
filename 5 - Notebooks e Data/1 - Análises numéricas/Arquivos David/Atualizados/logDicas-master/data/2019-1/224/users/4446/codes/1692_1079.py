from math import*

a=float(input("digitr a: "))
b=float(input("digitr b: "))
c=float(input("digitr c: "))
print("Entradas:", a,",", b, ",", c)


if( a>0 and b>0 and c>0):
	if(a<b+c and b<c+a and c<a+b):
		p= (a+b+c)/ 2.0
		area= sqrt(p * (p - a) * (p - b) * (p - c))
		area=round(area, 3)
		print ("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
	