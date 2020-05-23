from numpy import *
from numpy.random import *

matriz = array(eval(input("Matriz de horas: ")))

vetor = zeros(7,dtype=int)

for i in range(7):
	vetor[i] = sum(matriz[:,i])
	
for i in range(7):
	if vetor[i] == max(vetor):
		print(i + 1)