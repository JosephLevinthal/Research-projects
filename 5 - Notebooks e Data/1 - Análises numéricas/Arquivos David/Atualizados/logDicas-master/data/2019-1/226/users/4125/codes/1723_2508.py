from math import*
n = int(input("sigite os n primeiros termos: "))

soma = 3
i = 2
j = 0
while(1<n):
	soma = soma + ((-1)**j)*(4/(i*(i + 1)*(i + 2)))
	i = i + 2
	j = j + 1
	n = n -1
print(round(soma,8))