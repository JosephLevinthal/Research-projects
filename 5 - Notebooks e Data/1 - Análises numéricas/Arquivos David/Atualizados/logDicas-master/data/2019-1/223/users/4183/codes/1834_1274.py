from numpy import *
from numpy.linalg import *
n = int(input("Insira um numero: "))
m = ones((n,n),dtype=int)
for i in range(n):
	for j in range(n):
		m[i,j] = min(i,j) + 1
print(m)