#entrada de um numero inteiro
z = int(input("Digite um numero inteiro: "))
i = 0
soma = 0
while (i < z-1):
	r = z%(i + 1)
	if (r == 0):
		div = (i+1)
		soma = soma + div
		print(div)
	i = i+1
if (soma == z):
	print("PERFEITO")	
else:
	print("NAO PERFEITO")