from math import *
k = int(input("insira o numero:"))
soma = 0
i = 0
fim = k


while(k > i):
	soma = soma + 1/(factorial(i))
	i = i + 1
print(round(soma,8))
