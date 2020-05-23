n = int(input("Digite um numero: "))

soma = 3
i = 2
j = 0

while(1 < n):
	soma = soma + (4 / (i * (i + 1) * (i + 2))) * (-1) ** j
	i = i + 2
	j = j + 1
	n = n - 1
print(round(soma, 8))