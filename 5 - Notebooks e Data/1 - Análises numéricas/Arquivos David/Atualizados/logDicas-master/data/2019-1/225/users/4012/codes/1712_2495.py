# Introducao a Programacao de Computadores
# Criado em 15 / 05 / 2015
# @author: IComp / UFAM

# Primeiro input
num = int(input("Digite um numero: "))
while (num != -1):
	if (num % 2 == 0):
	mensagem = "PAR"
	else:
		mensagem = "IMPAR"
			
	print(mensagem)
	num = int(input("digite um numero: "))