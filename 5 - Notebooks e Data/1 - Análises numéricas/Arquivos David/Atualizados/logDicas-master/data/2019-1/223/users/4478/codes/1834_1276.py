from numpy import*
from numpy.linalg import*

func = array(eval(input("horas trabalhadas:")))
vetor = zeros(7, dtype=int)
for j in range (7):
	vetor[j] = sum(func[:,j])
for j in range (7):
	if(vetor[j]==max(vetor)):
		print(j+1)