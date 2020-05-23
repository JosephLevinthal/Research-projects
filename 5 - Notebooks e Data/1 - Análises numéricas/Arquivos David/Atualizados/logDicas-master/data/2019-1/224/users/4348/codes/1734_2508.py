from math import*
n = float(input("Numero: "))
soma = 3
i = 2
j = 0
while (1<n):
	soma = soma +(4/(i*(i+1)*(i+2))) *(-1)**j
	j = j+1
	i = i+2
	n = n-1
print(round(soma,8))