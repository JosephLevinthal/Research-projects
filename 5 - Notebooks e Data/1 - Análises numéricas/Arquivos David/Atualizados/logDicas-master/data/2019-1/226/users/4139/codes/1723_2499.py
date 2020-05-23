from math import*
a = int(input("numero: "))
soma = 0
i = 0
fim = a - 1
while(i <= fim):
	soma = soma + (1/factorial(i))
	i = i + 1

print(round(soma,8))