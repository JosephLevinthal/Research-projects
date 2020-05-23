from numpy import *
from numpy.linalg import *
mat = array(eval(input("Digite o numero de ht de cada funcionario: ")))
nlinhas = shape(mat)[0]
matrizht = zeros((nlinhas,7), dtype=int)
for i in range(nlinhas):
	for j in range(7):
		matrizht[i,j] = mat[i,j]
vetorht = zeros(nlinhas, dtype=int)
for i in range(nlinhas):
	vetorht[i] = sum(matrizht[i,:])
print(vetorht)