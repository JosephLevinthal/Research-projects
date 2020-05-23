from numpy import*
 
N= int(input("matriz quadrada:"))

mat=zeros((N,N), dtype=int)

for i in range(0,N):
	
	for j in range(0,N):
		mat[i,j]= min(i,j)+1

print(mat)
