from math import *
x=float(input("numero real: "))
k=int(input("termo da serie: "))
y=x
t=0
k=1
while (k > 0):
	t=t + 1
	y=k+ (y ** k) / factorial(y)
	k=k+2

print(round(k,9))