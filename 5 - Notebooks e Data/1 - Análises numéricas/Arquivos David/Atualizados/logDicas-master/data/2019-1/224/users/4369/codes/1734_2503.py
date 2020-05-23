from math import *
n = float(input("Digite o numero de termos: "))
i = 1
c = 0
soma = 0

while c < n:
	sinal = (-1) ** c
	soma = soma + (sinal * (4)) / (i)
	c = c + 1
	i = i + 2
print(round(soma, 8))



