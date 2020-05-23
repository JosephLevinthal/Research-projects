num = int(input("valor: "))

while(num != -1):
	if((num % 2) == 0):
		mensagem = "PAR"
	else:
		mensagem = "IMPAR"

	print(mensagem)
	
	num = int(input("valor: "))