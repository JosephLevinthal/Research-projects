
n = int(input("Insira o numero natural: "))

soma = 0
i = 0

while(n > i):
	
	soma = soma +(12 ** 0.5)*((-1)**i)*(1 / ((2 * i + 1) * (3 ** i)))
	i = i + 1

print(round(soma , 8))