from numpy import*
from numpy.linalg import*
n=int(input())
mat=zeros((n,n),dtype=int)
j=0
for i  in range(n):
	for j in range(n):
		if i==j:
			mat[i,j]=i+1
		if i<j:
			mat[i,j]=i+1
		if i >j:
			mat[i,j]=1+j
print(mat)
		