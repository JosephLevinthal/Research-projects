from math import*
k = int(input("Digite um numero natural: "))
e = 0
soma = 0
while( e < k):
	soma = soma + ((1) / (factorial(e)))
	e = e +1
print(round(soma, 8))