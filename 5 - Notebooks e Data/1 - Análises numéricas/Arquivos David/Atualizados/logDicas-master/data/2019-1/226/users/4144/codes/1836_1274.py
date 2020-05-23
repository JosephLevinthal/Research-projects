from numpy import *
N = int(input("digite um nro natural: "))
mat = zeros((N,N), dtype=int)
for i in range(N):
	for j in range(N):
		mat[i,j] = min(i,j) + 1
print(mat)