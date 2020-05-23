from numpy import *
from numpy.linalg import *

notas = array(eval(input("Matriz de notas: ")))

for i in range(notas):
	for j in range(notas):
		notas = max(notas)

print(notas)