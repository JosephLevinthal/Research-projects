from numpy import *
from numpy.linalg import *

matriz = array(eval(input('Matriz: ')))
N = shape(matriz)[0]
M = zeros(N, dtype=int)

for i in range(N):
	M[i] = sum(matriz[i,:])
	
print(M)