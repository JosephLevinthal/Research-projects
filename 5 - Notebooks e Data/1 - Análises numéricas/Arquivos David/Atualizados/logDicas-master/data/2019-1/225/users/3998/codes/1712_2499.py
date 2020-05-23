from math import *
k = float(input("numero natural: "))
soma = 0      #variavel acumuladora
i = 0         #variavel contadora
while (i < k):
	soma = soma + 1 / factorial(i)
	i = i +1
print(round(soma,8))
