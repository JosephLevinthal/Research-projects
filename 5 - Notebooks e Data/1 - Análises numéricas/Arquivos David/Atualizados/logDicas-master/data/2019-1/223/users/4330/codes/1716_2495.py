# Introducao a Programacao de Computadores
# Criado em 15 / 05 / 2015
# @author: IComp / UFAM

# Primeiro input
num = int(input("Digite um numero: "))

# Laco de repetica
while (num != -1 ):
	
	if ((num % 2) == 0 ):
		
		mensagem = "PAR"
		
	else:
		mensagem = "IMPAR"
	
	print(mensagem)
	
	# Inputs seguintes
	num = int(input("Digite um numero: "))

	