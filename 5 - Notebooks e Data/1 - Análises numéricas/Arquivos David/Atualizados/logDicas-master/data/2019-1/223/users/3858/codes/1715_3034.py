from math import *
x = float(input())

if(x>=-4 and x<0):
	x = abs(x) ** (1/2)
	print(round(x,4))
elif(x>0 and x<=4):
	print(round(sqrt(x),4))
elif(x==0):
	print(0)
else:
	print("entrada invalida")

	
	
