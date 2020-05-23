from numpy import*
from numpy.linalg import*

matriz = array(eval(input("matriz:")))
somatorio = 0

for i in range(shape(matriz)[0]):
	for j in range(shape(matriz)[1]):
		if (i == j):
			somatorio = somatorio + matriz[i, j]
print(round(somatorio,2))
