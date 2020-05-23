from numpy import*
from numpy.linalg import*

matriz = array(eval(input("Insira a matriz: ")))

vet = zeros(matriz.shape[0], dtype=int)

for i in range(matriz.shape[0]):
	vet[i] = sum(matriz[i,:])
	
print(vet)