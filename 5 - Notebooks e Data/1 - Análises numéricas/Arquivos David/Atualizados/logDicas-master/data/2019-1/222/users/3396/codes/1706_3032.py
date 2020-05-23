from math import*
x = float(input("x:"))
if(x<=0):
	fx= 0
elif(x>0 or x<=1):
	fx= 1
elif(x>1 or x<=2):
	fx= x**1/2
elif(x>2):
	fx= x**1/3
print(round(fx, 4))