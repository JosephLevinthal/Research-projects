x=float(input("valor de x:"))
if(x<=-1) or (x>=1):
	msg=x
	print(round(msg,2))
elif(-1<x<0) or (0<x<1):
	msg=1
	print(round(msg,2))
elif(x==0):
	msg=2
	print(round(msg,2))
