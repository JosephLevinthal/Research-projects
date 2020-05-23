from math import *
k=float(input("numero k: "))
e= 1
c=1
soma= 0
if (k==1):
	e=1.0
	print(e)
else:
	while c<k:
		soma= soma + (1)/factorial(c)
		c= c+1
	e= e+ soma
	print(round(e, 8))
