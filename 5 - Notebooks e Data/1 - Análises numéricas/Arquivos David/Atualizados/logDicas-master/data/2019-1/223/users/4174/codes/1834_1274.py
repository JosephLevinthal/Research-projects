from numpy import *
from numpy.linalg import *

N = int(input("dimensao:"))

matriz = zeros((N,N), dtype=int)

for i in range (0,N):
	for j in range(0,N):
		matriz[i,j] =  min(i,j)+ 1
		
print(matriz)		



