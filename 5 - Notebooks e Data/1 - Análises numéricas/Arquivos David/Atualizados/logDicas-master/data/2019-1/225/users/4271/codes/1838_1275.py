from numpy import *
from numpy.random import *
mat = array(eval(input("Matriz de horas: ")))
vet = zeros(mat.shape[0], dtype=int)
for i in range(mat.shape[0]):
	vet[i] = sum(mat[i,:])
print(vet)