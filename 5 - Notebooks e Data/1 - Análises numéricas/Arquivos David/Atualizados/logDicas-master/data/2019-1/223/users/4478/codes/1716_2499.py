k = int(input("valor de k: "))

soma = 1
i=1
while(i<k):
	from math import factorial
	f = factorial(i)
	soma = soma + 1**i/f
	i = i+1
print(round(soma,8))
