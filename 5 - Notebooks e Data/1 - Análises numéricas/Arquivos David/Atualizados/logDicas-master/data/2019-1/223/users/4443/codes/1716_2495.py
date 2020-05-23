# Introducao a Programacao de Computadores
# Criado em 15 / 05 / 2015
# @author: IComp / UFAM

# Primeiro input
num = int(input("Digite um numero: "))

# Laco de repeticao
while (num != -1): #Condicao do laco, se o valor -1 for digitado, ele para.
	resto = num%2 # verificacao se o num eh par
	if (resto == 0): #se for par, o resto da divisao eh zero
		mensagem = "PAR"
	else: #se o resto da divisao nao for zer, o numero eh impar
		mensagem = "IMPAR"
	
	print(mensagem)
	
	# Inputs seguintes
	num = int(input("Digite um numero: "))
