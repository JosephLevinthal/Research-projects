from numpy import *
from numpy.linalg import *

n = int(input("Numero: "))

x = zeros((n,n), dtype=int)

for i in range(n):
	for j in range(n):
		if(i == j):
			x[i,j] = i + 1
		elif(i > j):
			x[i,j] = j + 1
		elif(i < j):
			x[i,j] = i + 1
			
print(x)			