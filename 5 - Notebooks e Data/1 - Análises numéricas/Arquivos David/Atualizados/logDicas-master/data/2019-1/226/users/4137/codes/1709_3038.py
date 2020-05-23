from math import*
x = float(input("Valor de x:"))

if(x <= -1 or x >= 1):
	print(round(abs(x**0.5), 2))
elif( x > -1 and x < 0 or x > 0 and x < 1):
	print(round(abs(x), 2))
elif( x == 0):
	print(0)