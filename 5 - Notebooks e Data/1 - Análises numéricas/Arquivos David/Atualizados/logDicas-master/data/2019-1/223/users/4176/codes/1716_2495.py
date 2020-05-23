num = int(input("Digite um numero: "))

# Laco de repeticao
while (num != -1):
	# Verifica se valor eh divisivel por 2
	if (num % 2):
		mensagem = "IMPAR"
	else:
		mensagem = "PAR"
	
	print(mensagem)
	
	# Inputs seguintes
	num = int(input("Digite um numero: "))
