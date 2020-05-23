from math import*
x=float(input("Digite um numero: "))
k=1
e=1
while(k<x):
	e=e+1/factorial(k)
	k=k+1
print(round(e,8))	