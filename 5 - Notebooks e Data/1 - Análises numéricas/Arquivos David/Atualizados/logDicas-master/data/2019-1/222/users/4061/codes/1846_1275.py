from numpy import*

matriz = array(eval(input("Digite: ")))
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]

vetor_nulo = zeros(linhas, dtype=int)


for i in range(linhas):
	for j in range(colunas):
		
		# Soma das linhas da matriz sendo atribuida ao vetor nulo
		
		vetor_nulo[i] = vetor_nulo[i] + matriz[i, j]
	
print(vetor_nulo)