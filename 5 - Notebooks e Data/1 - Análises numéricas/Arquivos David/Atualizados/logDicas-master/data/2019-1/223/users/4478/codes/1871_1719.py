from numpy import*
from numpy.linalg import*

matriz = array(eval(input("nota dos alunos: ")))
vetor = zeros(matriz.shape[0],dtype=int)
for i in range(matriz.shape[0]):
	vetor[i] = sum(matriz[i,:])
	media = sum(vetor)/
alunos = 0
for i in range (size(media)):
	if(i>=5):
		alunos = alunos +1
print(alunos)
