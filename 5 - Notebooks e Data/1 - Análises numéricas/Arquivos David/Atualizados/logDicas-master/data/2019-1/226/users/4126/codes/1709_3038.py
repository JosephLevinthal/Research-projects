from math import*
x = float(input("x:"))
if(x<=-1)or (x>=1):
	print(abs(round(x**(1/2))))
elif(-1<x<0)or (0<x<1):
	print(abs(round(x**(1/2))))
elif(x==0):
	print(abs(round(x**(1/2))))
else:
	print(invalido)


