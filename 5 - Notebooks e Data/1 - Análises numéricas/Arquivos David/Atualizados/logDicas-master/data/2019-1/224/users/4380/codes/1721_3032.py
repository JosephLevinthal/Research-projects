from math import *
x=float(input("number: "))
if(x<=0):
	print("0")
elif((x>0)and(x<=1)):
	print("1")
elif((x>1)and(x<=2)):
	print(round(x**(1/2),4))
elif(x>2):
	print(round(x**(1/3),4))