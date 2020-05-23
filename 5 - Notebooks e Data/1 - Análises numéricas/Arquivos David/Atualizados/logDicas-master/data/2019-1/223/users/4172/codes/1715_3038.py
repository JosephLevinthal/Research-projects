from math import*

x=float(input("valor de x: "))

if(x<0)or(x>0):
	if(x<=-1)or(x>=1):
		q=sqrt(abs(x))
		print(round(q,2))
	elif(-1<x<0)or(0<x<1):
		q=abs(x)
		print(round(q,2))
	elif(x==0):
		print(0)
		