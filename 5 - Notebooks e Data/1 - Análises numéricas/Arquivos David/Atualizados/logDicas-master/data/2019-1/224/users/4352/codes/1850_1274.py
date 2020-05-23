from numpy import*
from numpy.linalg import*
n = int(input("digite um numero: "))
m = zeros((n,n), dtype=int)
for i in range(n):
	for j in range(i,n):
		m[i,j] = i + 1
		m[j,i] = i + 1
print(m)