from numpy import *
matriz = array(eval(input("matriz: ")))
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]
matriz_nula = zeros((linhas, colunas), dtype=int)
vetor_nulo = zeros(colunas, dtype=int)


for i in range(colunas):
	for j in range(colunas):
		vetor_nulo[j] = matriz[j, i]

	vetor_nulo = sorted(vetor_nulo, reverse=True)
	
	matriz_nula[:, i] = vetor_nulo
	
print(matriz_nula)