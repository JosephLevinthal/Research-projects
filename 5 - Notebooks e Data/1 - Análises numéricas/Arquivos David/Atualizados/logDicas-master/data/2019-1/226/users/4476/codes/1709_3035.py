from math import*
x = float(input("valor de x: "))

if (x<0) or (x>=180):
	print("entrada invalida")
elif (0<=x<90) or (x==180):
	a = radians(x)
	b = sin(x)
	print(round(b, 4))
elif (90<=x<180) or (x==270):
	a = radians(x)
	b = cos(x)
	print(round(b, 4))