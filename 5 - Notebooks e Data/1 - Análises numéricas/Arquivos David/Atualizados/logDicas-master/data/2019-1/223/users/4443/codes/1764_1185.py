from numpy import *
g = array(eval(input("Digite os valores de glicose: "))) #coleta da quantidade de glicose

soma = 0 #variavel acumuladora da quantidade de pcts com glicemia acima de 99mg/dl
i = 0 #variavel contadora do laco
while (i < len(g)): #i percorre todas as posicoes do vetor de entradas 
	if(g[i] > 99): #testa a condicao para cada posicao
		print(i) #se verdade imprime o valor de indice g[i]
		soma = soma + 1 #incrementa a variavel cumuladora do n de pacientes
	i = i+1	#incrementa a variavel contador do laco
print(soma)		#printa a quantidade final de pessoas com valor superior ao lim