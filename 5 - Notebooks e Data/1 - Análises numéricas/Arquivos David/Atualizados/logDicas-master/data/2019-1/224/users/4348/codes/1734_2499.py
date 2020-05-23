from math import*
k = int(input("Digite o numero natural:"))
soma = 0 #acomuladora
i = 0 #contador
fim = k-1
while (i <= fim):
	soma = soma + (1/factorial(i))
	i = i + 1
print(round(soma,8))