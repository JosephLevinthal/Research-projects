from numpy import*
vetor = array(eval(input("tempo, entrandoADM, saindoADM, entrandoCHAO, saindoCHAO:")))

entrada_A = vetor[1]
saida_A = vetor[2]
entrada_C = vetor[3]
saida_C = vetor[4]

x = 0
while(x >= 0):
	vetor_1 = eval(input("tempo, entrandoADM, saindoADM, entrandoCHAO, saindoCHAO:"))
	x = vetor_1
	vetor_1 = array(vetor_1)
	entrada_A = entrada_A + vetor_1[1]
	saida_A = saida_A + vetor_1[2]
	entrada_C = entrada_C + vetor_1[3]
	saida_C = saida_C + vetor_1[4]	
	
print(entrada_A)
print(saida_A)
print(entrada_C)
print(saida_C)

		