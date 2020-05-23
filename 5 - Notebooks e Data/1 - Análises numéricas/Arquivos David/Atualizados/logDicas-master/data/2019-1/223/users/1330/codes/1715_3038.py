from math import *
x = float(input())

if(x<=-1 or x>=1):
	resultado = sqrt(abs(x))
elif((x<0 and -1<x) or (0<x and x<1)):
	resultado = abs(x)
else:
	resultado = 0
print(round(resultado,2))