from numpy import *

matriz = array(eval(input("Matriz: ")), dtype=float)
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]
n = colunas**2 - colunas
vetor = zeros(n, dtype=float)

k = 0

while k < n:
	for i in range(linhas):
		for j in range(colunas):
			if i != colunas-1-j:
				vetor[k] = matriz[i, j]
				k = k + 1

print(min(vetor))
