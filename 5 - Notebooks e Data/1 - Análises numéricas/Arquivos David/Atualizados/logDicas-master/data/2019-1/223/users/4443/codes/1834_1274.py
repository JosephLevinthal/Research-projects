from numpy import *
from numpy.linalg import *
z = int(input("Digite um numero inteiro maior que 0: "))
matriz = zeros((z, z), dtype=int)
for i in range(z):
	for j in range(z):
		if(i == j):
			matriz[i,j]= i+1
		elif(i < j):
			matriz[i,j]= i+1
		else:	
			matriz[i,j]= j+1
print(matriz)			