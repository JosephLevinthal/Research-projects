from numpy import *
from numpy.linalg import *
mat = array(eval(input("Digite o numero de ht de cada funcionario: ")))
nlinhas = shape(mat)[0]
matrizht = zeros((nlinhas,7), dtype=int)
for i in range(nlinhas):
	for j in range(7):
		matrizht[i,j] = mat[i,j]
vetorht = zeros(7, dtype=int)
for j in range(7):
	vetorht[j] = sum(matrizht[:,j])
for i in range(len(vetorht)):
	if(vetorht[i] == max(vetorht)):
		print(i+1)
