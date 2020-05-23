n = int(input("n. de termos: "))
soma = 0
i = 0
sinal = + 4
while (i < n):	
	soma = soma + sinal / (2*i + 1)
	sinal = - sinal
	i = i + 1
	
print(round(soma, 8))