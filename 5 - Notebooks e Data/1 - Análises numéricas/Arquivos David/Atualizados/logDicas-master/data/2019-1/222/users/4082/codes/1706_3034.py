import.mat
x= float(input())


if (x >= -4 and x <0):
	f= (x**0.5)
	fx= 0
elif(x=0):
	fx=0
elif(x>0 and x<=1):
	fx=(x**0.5)
else:
	fx='entrada invalida'
	print(fx)