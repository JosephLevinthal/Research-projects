from math import*

k = int(input("valor de x:"))
soma = 1
i = 1
while(i < k):
	soma = soma + (1/factorial(i))
	i = i + 1
	
print(round(soma,8))