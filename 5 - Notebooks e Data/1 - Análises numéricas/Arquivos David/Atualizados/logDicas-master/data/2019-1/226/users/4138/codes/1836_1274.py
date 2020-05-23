from numpy import *

N = int(input("dimensao da matriz:"))

mat = zeros((N,N),dtype=int)

for i in range (N):
	for j in range (N):
		if(i == j):
			mat[i,j] = i + 1
		elif(i < j):
			mat[i,j] = i + 1
		else:
			mat[i,j] = j + 1
			
print(mat)
			