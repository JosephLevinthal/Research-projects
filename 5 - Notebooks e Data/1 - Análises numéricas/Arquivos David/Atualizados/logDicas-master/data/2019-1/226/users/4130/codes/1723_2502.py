n = int(input("Numero de repeticoes: "))

soma = 0
i = 0

while(0 < n):
	soma = soma + (12 ** (1/2)) * ((1 / ((2 * i + 1) * (3 ** i)))) * ((-1) ** i)
	i = i + 1
	n = n - 1
print(round(soma, 8))