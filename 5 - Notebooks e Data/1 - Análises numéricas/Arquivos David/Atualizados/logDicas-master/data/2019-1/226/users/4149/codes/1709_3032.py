from math import *

x=float(input("entre com o valor de x: "))

a=sqrt(x)
b=x**(1/3)
if(x<=0):
	print(abs(0))
elif(x>0)and(x<=1):
	print(abs(1))
elif(x>1)and(x<=2):
	print(round(a,4))
elif(x>2):
	print(round(b,4))