from numpy import*
N = int(input("Digite o numero n: "))
vet = zeros((N,N), dtype=int)
g=1
for i in range(N):
	for j in range(N):
		if(i==j): #Diagonal principal
			vet[i,j] = g
		elif(i<j): #Direita da diagonal principal
			vet[i,j] =  g
	g = g+1
g=1
for j in range(N):
	for i in range(N):
		if(i>j):
			vet[i,j] = g
	g= g+1
print(vet)
			

			
			
			
			
	
