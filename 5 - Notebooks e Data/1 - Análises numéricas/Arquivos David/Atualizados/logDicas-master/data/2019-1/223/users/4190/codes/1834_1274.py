from numpy import *
from numpy.linalg import *

N = int(input())
M = zeros((N, N), dtype=int)

for i in range(N):
	for j in range(N):
		M[i, j] = min(i, j)+1
	
print(M)