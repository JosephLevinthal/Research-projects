from numpy import *
from numpy.linalg import *
n = int(input("Num: "))
mat = zeros((n,n), dtype=int)
for i in range(n):
	for j in range(n):
		mat[i,j] = min(i,j) + 1
print(mat)