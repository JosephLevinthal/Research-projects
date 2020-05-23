from math import *
n=int(input("digite um numero: "))
i=0
x=0
while(i<n):
	x= (x+1/factorial(i))
	i=i+1
print(round((x),8))