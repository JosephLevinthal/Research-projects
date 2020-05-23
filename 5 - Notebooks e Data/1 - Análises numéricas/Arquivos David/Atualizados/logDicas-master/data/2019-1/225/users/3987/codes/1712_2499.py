from math import *
k = float(input(":"))

soma = 0
i = 0

while(i < k):
	soma = soma + (1/factorial(i))
	i = i + 1
print(round(soma,8))