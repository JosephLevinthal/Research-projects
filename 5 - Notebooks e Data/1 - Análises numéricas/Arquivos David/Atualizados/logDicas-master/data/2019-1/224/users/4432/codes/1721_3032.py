from math import*
x=float(input("x   "))
if(x<=0):
	print("0")
elif(x>0)and(x<=1):
	print("1")
elif(x>1)and(x<=2):
	z=sqrt(x)
	print(round(z,4))
else:
	if(x>2):
		z=x**(1/3)
		print(round(z,4))
	