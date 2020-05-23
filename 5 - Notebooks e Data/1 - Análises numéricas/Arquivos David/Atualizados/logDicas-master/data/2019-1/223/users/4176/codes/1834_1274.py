from numpy import *
from numpy.linalg import *

N = int(input("um numero natural N:"))
matriz = ones((N,N), dtype=int)
A = shape(matriz)[1]
B= 1
h = 0
for  h in range(A):
	for i in range(B,A):
		for j in range(B,A):
			matriz[i,j] = matriz[i,j] + 1
	B = B + 1
		
print(matriz)
