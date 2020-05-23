from math import factorial
n=int(input("digite um numero natural:"))
e=1
indice=1
while(indice<n):
	e=e+(1/factorial(indice))
	indice=indice+1
print(round(e, 8))