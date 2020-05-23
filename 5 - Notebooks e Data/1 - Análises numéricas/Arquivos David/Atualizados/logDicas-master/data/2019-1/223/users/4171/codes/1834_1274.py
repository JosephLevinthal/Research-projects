from numpy import *
from numpy.linalg import*

n = int(input("n: "))
b = zeros((n,n), dtype = int)
for i in range(n):
	for j in range(n):
		b[i,j] = min(i,j) + 1
print(b)