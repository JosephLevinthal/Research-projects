n = int(input("numero: "))
soma = 3
i = 1
fim = n

while(i < fim ):
	soma = soma + ((-1)** (1+i)) * (4 / (( i * 2) * (i * 2 + 1) * (i * 2 + 2)))
	i = i + 1
print(round(soma, 8))	