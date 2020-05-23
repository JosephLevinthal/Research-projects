from math import*

n = int(input("valor de n: "))

soma = 0
i = 0
sinal = +1

while (i<=n-1):
	soma = soma + sinal * 1/((2*i+1)*(3**i)) *sqrt(12)
	sinal = - sinal
	i = i + 1
print(round(soma, 8))