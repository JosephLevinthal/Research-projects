
n = int(input("repeticao do termo: "))
soma = 0
i = 0
expoente = 0
sinal = 1
while(i < n):
	d = ((2 * i) + 1) * (3**expoente)
	x = 12**(1 / 2) * (sinal * 1)/d
	soma = soma + x 
	i = i + 1
	sinal = sinal * (-1)
	expoente = expoente + 1
print(round(soma, 8))