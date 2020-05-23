from numpy import*
from numpy.linalg import*

matriz = array(eval(input("nota dos alunos: ")))
vetor = zeros(matriz.shape[0], dtype=int)
for i in range (matriz.shape[0]):
	vetor[i] = sum(matriz[i,:])
	media = sum(vetor)
print(round(media,2))