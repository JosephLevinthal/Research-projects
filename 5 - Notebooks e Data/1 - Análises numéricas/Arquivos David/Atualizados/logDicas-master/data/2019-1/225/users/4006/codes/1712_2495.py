# Introducao a Programacao de Computadores
# Criado em 15 / 05 / 2015
# @author: IComp / UFAM

# Primeiro input
num = int(input("Digite um numero: "))

# Laco de repeticao
while (num != -1):
	# Verifica se valor eh divisivel por 2
	if (num / 2 ):
		num = 2,4 ,6 ,8
		mensagem = "PAR"
	else:
		mensagem = "IMPAR"
	
	print(mensagem)
	
	# Inputs seguintes
	num = int(input("Digite um numero: "))
