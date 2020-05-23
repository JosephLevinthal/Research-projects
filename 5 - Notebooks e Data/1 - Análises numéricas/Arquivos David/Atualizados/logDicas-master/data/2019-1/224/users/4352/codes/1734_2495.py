n = int(input("digite o numero: "))
while (n != -1):
	if n % 2 == 0:
		mensagem = "PAR"
	else: 
		mensagem = "IMPAR"
	print(mensagem)
	n = int(input("digite o numero: "))
	