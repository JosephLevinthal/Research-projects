from math import *
n=int(input("numero inicial: "))
i=1
while(n>0):
	i=(factorial(n))+i
	n=n-1
print(round(i,8))