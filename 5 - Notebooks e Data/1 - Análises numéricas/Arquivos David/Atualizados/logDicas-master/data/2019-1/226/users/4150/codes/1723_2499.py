from math import*

n= int(input("digite o numero natural: "))

soma = 0
i = 0
fim = n-1

while (i<=fim):
	soma = soma + (1/factorial(i))
	i = i+1
print(round(soma, 8))