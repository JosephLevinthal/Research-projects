from math import factorial
k=int(input("Valor de k: "))
cont=0
numerador=0
result=0

while(cont<k):
	result=result+(1/factorial(numerador))
	numerador=numerador+1
	cont=cont+1

print(round(result, 8))	