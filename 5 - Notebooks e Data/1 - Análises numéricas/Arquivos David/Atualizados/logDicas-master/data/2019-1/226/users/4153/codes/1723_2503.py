n = int(input("Insira o numero natural: "))

soma = 0
i = 0

while(n > i):
	soma = soma + ((-1)**i) * (4/ (2  *  i + 1))
	i = i + 1
print(round(soma ,8))