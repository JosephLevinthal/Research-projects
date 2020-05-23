from math import *
x = float(input("X: "))

if (x <= 0):
	f = 0
elif (x > 0 and x < 1):
	f = 1
elif (x > 1 and x <= 2):
	f = sqrt(x)
elif (x > 2):
	f = pow(x,1/3)

print(round(f,4))