from numpy import *
matriz = array(eval(input("matriz: ")))
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]
matriz_nula = zeros((linhas, linhas), dtype=int)
vetor_nulo = zeros(colunas, dtype=int)
for i in range(colunas):
	for j in range(colunas):
# Atribuir cada coluna ao vetor nulo
		vetor_nulo[j] = matriz[j, i]
# Ordenando o vetor
	vetor_nulo = sorted(vetor_nulo, reverse=True)
# Atribuindo o vetor na matriz
	matriz_nula[:, i] = vetor_nulo
	
print(matriz_nula)