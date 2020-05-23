n = int(input("Digite um numero natural: "))
i = 0
x = 1
soma = 0
while(n > 0):
	soma = soma + (4/x) * (-1)**i
	x = x + 2
	n = n - 1
	i = i + 1
print(round(soma,8))
	