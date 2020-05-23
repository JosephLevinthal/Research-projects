from math import *
a = float(input("asasd "))
b = float(input("asasd "))
c = float(input("asasd "))
s = (a+b+c)/2
print('Entradas: ',a,", ",b,", ",c)
if((a>0) and (b>0) and (c>0)):
	if (a<b+c)and(b<c+a)and(c<a+b):
		print("Area: ",round(sqrt(s*(s-a)*(s-b)*(s-c)),3))
	else:
		print("Area: invalida")
else:
		print("Area: invalida")