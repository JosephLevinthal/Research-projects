from numpy import*
from numpy.linalg import*

matriz = array(eval(input("n de horas:")))

vetor = (shape(matriz)[0])
total = zeros(vetor, dtype=int)

for i in range(vetor):
	total[i] = sum(matriz[i,:])
print(total)

