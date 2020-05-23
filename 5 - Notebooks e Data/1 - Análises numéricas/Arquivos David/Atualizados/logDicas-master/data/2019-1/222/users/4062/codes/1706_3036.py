x=float(input("valor de x: "))
if(x<=-1) or (x>=1):
	print(round(x, 2))
elif(-1<x) and (x<0) or (0<x) and (x<1):
	print(round(1, 2))
elif(x==0):
	print(round(2, 2))
	