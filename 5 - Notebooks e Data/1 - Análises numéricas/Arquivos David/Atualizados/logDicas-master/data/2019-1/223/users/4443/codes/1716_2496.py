# Primeiro input
num = int(input("Digite um numero: "))

soma = 0 #variavel acumuladora, para cada repeticao ela era acumular o valor calculado
# Laco de repeticao
while (num != -1): #condicao do laco, o numero deve ser diferente de 1
	soma = soma + num # se o num for != de -1, ele deve ser somado com a soma anterior 
		# Inputs seguintes
	num = int(input("Digite um numero: ")) #se num for != de -1, deve a o laco pede outro num
print(soma) #qndo o valor -1 for digitado, o laco termina e o valor total eh impresso