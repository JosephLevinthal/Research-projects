from numpy import *
from numpy.random import *
mat = array(eval(input("Matriz de horas: ")))
vet = zeros(7, dtype=int)
for i in range(7):
	vet[i] = sum(mat[:,i])
for i in range(7):
	if vet[i] == max(vet):
		print(i + 1)
	