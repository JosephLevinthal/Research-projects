from numpy import *
from numpy.linalg import *

N = int(input("Dimensao da matriz: "))
# Cria matriz de zeros, no formato inteiro
mat = zeros((N,N), dtype=int)
# Preenchimento da matriz
for i in range(N):
	for j in range(N):
# Verifica se diagonal principal
		if (i == j):
			mat[i,j] = i+1
# Verifica se termo estah ACIMA
		elif (i < j):
			mat[i,j] = i+1
# termos abaixo da dp
		else:
			mat[i,j] = j+1

	
print(mat)