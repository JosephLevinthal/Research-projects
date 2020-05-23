x=float(input("digite um numero: "))
if(x<=-1) or (x>=1):
	print(round(x,2))
elif(-1<x) and (x<0) or (0<x) and (x<1):
	print(1)
elif(x==0):
	print(2)