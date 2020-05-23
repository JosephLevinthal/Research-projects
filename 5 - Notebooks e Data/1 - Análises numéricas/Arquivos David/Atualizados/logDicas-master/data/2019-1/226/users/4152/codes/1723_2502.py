from math import *
#Termo Geral = 1 / i * 3 ** e
n = int(input("Digite aqui o total de termos: "))
i = 0
fim = n - 1
soma = 0
while (i <= fim):
	p = sqrt(12)
	soma = soma + (-1) ** (i) * 1 / ((2 * i + 1) * 3 ** i)  * p
	i = i + 1
print(round(soma, 8))