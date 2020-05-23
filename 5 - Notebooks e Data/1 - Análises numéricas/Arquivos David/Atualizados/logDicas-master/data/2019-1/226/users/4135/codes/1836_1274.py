from numpy import*
N = int(input("Dimensao da matriz: "))

mat= zeros((N,N),dtype=int)


for i in range(N):
	for j in range(N):
		mat[i,0]=1
		mat[0,j]=1
		if(i<j or i==j):
		   mat[i,j]=i+1
		elif(i>j):
			mat[i,j]=j+1
		
			
					
print(mat)	
	