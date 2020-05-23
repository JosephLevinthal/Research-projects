from numpy import *
N = int(input("Dimensao da matriz: "))
mat= ones((N,N), dtype= int)
j=1
k=2

for i in range(1,N): 
	while(j < N):
		mat[i,j]=i+1
		j=j+1
	j=k
	k=k+1
i=1
k=2
for j in range (1,N):
	while(i<N):
		mat[i,j]=j+1
		i=i+1
	i=k
	k=k+1
	
print(mat)