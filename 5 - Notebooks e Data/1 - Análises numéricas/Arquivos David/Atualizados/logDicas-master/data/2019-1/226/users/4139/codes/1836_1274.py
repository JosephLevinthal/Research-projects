from numpy import*
from numpy.linalg import*

n = int(input("numero da matriz: "))
mat = ones((n,n),dtype=int)

nov = zeros((n,n),dtype=int)

for i in range(n):
	for j in range(n):
		nov[i,j] = min(i,j) + 1

print(nov)