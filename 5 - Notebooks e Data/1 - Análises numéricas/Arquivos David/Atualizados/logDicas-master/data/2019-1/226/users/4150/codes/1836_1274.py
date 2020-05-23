from numpy import*
from numpy.linalg import*

n = int(input("digite: "))
mat = zeros((n,n), dtype=int)

mat = ones((n,n), dtype=int)
new = zeros((n,n), dtype=int)

for i in range(n):
	for j in range(n):
		new[i,j] = min(i,j)+1

print(new)