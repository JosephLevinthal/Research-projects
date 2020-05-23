n = int(input("valor de n: "))

soma = 3
i = 1
sinal = +1

while (i<=n-1):
	soma = soma + sinal * 4/((2*i)*(2*i+1)*(2*i+2))
	sinal = - sinal
	i = i + 1
print(round(soma, 8))
