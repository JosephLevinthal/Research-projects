from math import*
x = eval(input("angulo: "))
k = int(input("serie: "))
n = 1
cosx = 1
while n<k:
	if n%2 !=0:
		cosx = cosx - (x**(2*n))/factorial(2*n)
	else:
		cosx = cosx + (x**(2*n))/factorial(2*n)
	n = n + 1
print(round(cosx, 10))