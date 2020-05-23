from math import factorial
k=int(input("digite n: "))
e=1
indice=1
while(indice<k):
	e=e+(1/factorial(indice))
	indice=indice+1
print(round(e,8))