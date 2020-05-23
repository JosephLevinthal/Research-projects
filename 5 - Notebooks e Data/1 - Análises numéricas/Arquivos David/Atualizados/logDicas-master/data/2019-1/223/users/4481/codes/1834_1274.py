from numpy import*
from numpy.linalg import*
a = int(input('digite: '))
b = zeros((a,a), dtype=int)
for i in range(a):
	for j in range(a):
		b[i,j] = min(i,j) + 1
print(b)
	


