from math import*
x = float(input("x:"))
if(x<=0):
	print(abs(round(0,4)))
elif(0<x<=1):
	print(abs(round(1,4)))
elif(1<x<=2):
	print(abs(round(x**(1/2),4)))
elif(x>2):
	print(abs(round(x**(1/3),4)))