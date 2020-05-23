from numpy import*
from numpy.linalg import*

a = int(input("Insira um numero:"))

mat = zeros((a,a),dtype=int)

for i in range (a):
	for j in range (a):
			mat[i,j] = min(i,j) + 1

print(mat)