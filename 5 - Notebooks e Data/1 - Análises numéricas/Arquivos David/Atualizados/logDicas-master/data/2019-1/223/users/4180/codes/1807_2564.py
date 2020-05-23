#Leitura
from numpy import*
Ngols = array(eval(input("Numero de gols efetuados por partida: ")))
Ngols2 = array(eval(input("Numero de gols efetuados pelo adversario: ")))
#Vetor de contagem
result = zeros(3 , dtype = int)
#Condição
for i in range(0 , size(Ngols)):
	#Vitorias
	if(Ngols[i] > Ngols2[i]):
		result[0] = result[0] + 1
	#Empates
	elif(Ngols[i] == Ngols2[i]):
		result[1] = result[1] + 1
	#Derrotas
	elif(Ngols[i] < Ngols2[i]):
		result[2] = result[2] + 1
	# O Caralho do Resultado
print(result)
	

