from numpy import*
from numpy.linalg import*
matriz = array([[10,8,2],[20,16,4],[40,32,8]])
n = shape(matriz)
pinc = 0
for j in range(matriz):
	for i in range(matriz):
		if (i == j):
			princ = princ + sum(matriz)
	print(pinc)