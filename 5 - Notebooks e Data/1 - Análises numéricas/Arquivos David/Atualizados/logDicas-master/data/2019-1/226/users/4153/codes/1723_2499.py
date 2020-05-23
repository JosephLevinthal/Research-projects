from math import *

k = int(input("Insira o valor de k: "))
soma = 0
i = 0
f = k - 1

while (i <= f):
	soma = soma + 1/(factorial(i))
	i = i + 1

print(round(soma, 8))