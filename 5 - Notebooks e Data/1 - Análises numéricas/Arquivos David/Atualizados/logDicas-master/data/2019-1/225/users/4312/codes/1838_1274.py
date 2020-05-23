from numpy import*
from numpy.linalg import*

n = int(input("Tamanho da matiz: "))

mat = zeros((n,n), dtype=int)

for i in range(0, n):
	for j in range(0, n):
		mat[i, j] = min(i, j)+1
		
print(mat)