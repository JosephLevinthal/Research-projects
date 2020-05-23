x=float(input("valor de x: "))
if(x<=-1)or (x>=1):
	msg=x**2
	print(round(msg,4))
elif(-1<0) and (x>-1) and (x<0):
	msg=x
	print(round(msg,4))
elif(0<1) and (x>0) and (x<1):
	msg=x
	print(round(msg,4))
elif(x==0):
	msg=1
	print(round(msg,4))