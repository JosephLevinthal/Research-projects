y=float(input("a"))
b=float(input("b"))
c=float(input("c"))

from math import*
s=(y+b+c)/2.0

a=sqrt(s*(s-y)*(s-b)*(s-c))
a=round(a,3)
h="invalida"

if(y>=b+c) or (b>=y+c) or (c>=b+y) or (y<0) or (b<0) or (c<0):
	print("Entradas:", y, ",",b, ",",c)
	print("Area:",h)
else:
	print("Entradas:", y, ",",b, ",",c)
	print("Area:",a)
	

