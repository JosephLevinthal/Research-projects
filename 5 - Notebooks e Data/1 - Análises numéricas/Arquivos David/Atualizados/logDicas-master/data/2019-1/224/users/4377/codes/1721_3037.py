x=float(input("x"))
x=round(x,4)
if(x<=-1 or x>=1):
	x=x**2
	print(x)
elif(-1<x<0 or 0<x<1):
	x=x
	print(x)
elif(x==0):
	x=1
	print(x)