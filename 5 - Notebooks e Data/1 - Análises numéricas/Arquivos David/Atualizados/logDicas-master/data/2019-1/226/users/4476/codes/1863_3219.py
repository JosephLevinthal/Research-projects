from numpy import *
from numpy.linalg import *

M = array(eval(input("Digite a matriz: ")))

for i in range(M):
	for j in range(M):
		if i == j:
			M[i] = 