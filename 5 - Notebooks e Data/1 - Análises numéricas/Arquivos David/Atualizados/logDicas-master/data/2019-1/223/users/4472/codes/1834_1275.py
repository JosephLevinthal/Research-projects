from numpy import *
from numpy.linalg import *

matriz = array(eval(input("Matriz de Horas: ")))

vetor = zeros(matriz.shape[0], dtype=int)

for i in range(matriz.shape[0]):
	vetor[i] = sum(matriz[i,:])
	
print(vetor)

