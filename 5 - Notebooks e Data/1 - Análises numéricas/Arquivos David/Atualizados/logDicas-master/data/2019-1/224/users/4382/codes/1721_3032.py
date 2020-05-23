from math import*
x = float(input("valor de x : "))
if(x <= 0 ):
	fx = 0
	print(round(fx,4))
elif(0 < x <= 1):
	fx = 1
	print(round(fx,4))
elif(1< x <= 2):
	fx = x**(1/2) 
	print(round(fx,4))
elif(x > 2 ):
	fx = x ** (1/3)
	print(round(fx,4))
