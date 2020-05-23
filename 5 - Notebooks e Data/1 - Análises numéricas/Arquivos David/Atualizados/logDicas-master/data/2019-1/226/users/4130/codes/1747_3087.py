x = int(input("Digite um numero: "))

soma = 0
i = 0

while(x != 0):
	if(x % 2 == 0):
		soma = soma + 2
		print(soma)
	else:
		soma = soma + 2
		print(soma)
print(round(soma, 2))