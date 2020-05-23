n = int(input("valor: "))
soma = 0
i = 0
sinal = +1
while (i<=n-1):
	soma = soma + sinal * 4/(2*i+1)
	sinal = - sinal
	i = i + 1
print(round(soma, 8))
	