m = int(input("Digite os movimentos da tartaruga para a direita ou esquerda: "))
c = 0
soma = 0
while m != 0:
	m = int(input("Digite os movimentos da tartaruga para a esquerda(numero negativo) ou direita(numero positivo: "))
	c = c + 1
	soma = soma + (m * c)
	if m > 0:
		print(soma)
		print("Direita")
		
	else:
		print(soma)
		print("Esquerda")

	