from numpy import *
from numpy.linalg import *
n=int(input("digite: "))
mat=zeros((n,n), dtype=int)
for i in range(n):
	for j in range(n):
		if(i>j):
			mat[i,j]=j+1
		elif(i<j):
			mat[i,j]=i+1
		elif(i==j):
			mat[i,j]=i+1
print(mat)
			