from numpy import*
N = int(input("Matriz: "))
#matriz de zeros
z = zeros((N,N), dtype=int)
c = 1 
for i in range(N):
	for j in range(N):
		if (i < j):
			z[i,j] = c
		elif(i == j):
			z[i,j] = c
	c = c + 1
c = 1
for j in range(N):
	for i in range(N):
		if (j < i):
			z[i,j] = c
	c = c + 1		
print(z)	