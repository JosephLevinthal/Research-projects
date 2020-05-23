from numpy import*
from numpy.linalg import*
n=int(input("Entre com um numero:"))
mat=ones((n,n),dtype=int)
linha=shape(mat)
for i in range(n):
	for j in range(n):
		if (i<j):
			mat[i,j]=i+1
		elif(j>i):
			mat[i,j]=j+1
		else:
			mat[i,j]=j+1
print(mat)
	