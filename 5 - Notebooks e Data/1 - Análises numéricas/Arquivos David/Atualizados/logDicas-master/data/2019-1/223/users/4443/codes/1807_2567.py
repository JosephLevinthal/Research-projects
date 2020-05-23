from numpy import * #importa a biblioteca para trabalhar com vetores
z = int(input("Digite um numero maior que 1: ")) #coleta do numero inteiro

for i in range(z): #i percorre todas as posicoes do tamanho do vetor
	print("*"*(z-i)) #imprime * o numero de vezes da maior para a menor quantidade
	
for i in range(z): #i percorre todas as posicoes do tamanho do vetor
	print("*"*(i+1)) ##imprime * o numero de vezes da menor para a maior quantidade
		
