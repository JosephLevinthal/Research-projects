from math import*

k = int(input("quantidade de termos:"))

soma = 0
i = 0
fim = k - 1

while (i <= fim):
	soma = soma + 1 / factorial(i)
	i = i + 1
print(round(soma, 8))