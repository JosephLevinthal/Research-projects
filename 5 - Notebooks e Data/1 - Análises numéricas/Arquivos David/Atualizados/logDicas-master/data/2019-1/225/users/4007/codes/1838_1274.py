from numpy import *
from numpy.linalg import *

n = int(input("dimensao:"))
mat = ones((n,n), dtype=int)
j = 1
k = 2

for i in range(1,n):
	while(j<n):
		mat[i,j]=i+1
		j = j + 1
	j=k
	k = k + 1

i = 1
k = 2

for j in range(1,n):
	while(i<n):
		mat[i,j] = j+1
		i = i +1
	i = k
	k = k + 1

print(mat)










	