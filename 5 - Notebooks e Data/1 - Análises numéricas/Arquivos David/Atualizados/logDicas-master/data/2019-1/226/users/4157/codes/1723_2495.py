
# Primeiro input
num = int(input("Digite um numero: "))

# Laco de repeticao
while (num > -1):
	x = num % 2 
	if (x== 0):
		mensagem = "PAR"
	else:
		mensagem = "IMPAR"
	
	print(mensagem)
	
	num = int(input("Digite um numero: "))
