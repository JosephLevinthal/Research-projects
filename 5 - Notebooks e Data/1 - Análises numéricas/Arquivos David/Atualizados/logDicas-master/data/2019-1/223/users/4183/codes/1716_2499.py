from math import *
k = int(input("Digite o valor de k: "))
cont = 1
soma = 1
fact = 1
while(k > cont):
	soma = soma + (1/factorial(fact))
	fact = fact + 1
	cont = cont + 1
print(round(soma,8))