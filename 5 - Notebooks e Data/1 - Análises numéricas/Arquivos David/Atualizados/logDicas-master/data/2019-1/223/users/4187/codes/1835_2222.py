from numpy import *
from numpy.linalg import *

# "N" eh a dimencao da matriz 
N = int(input("N:"))

matriz = zeros((N,N), dtype=int)

for i in range(N):
	for j in range(N):
		elemento = int(input("elemento:"))
		matriz[i,j] = elemento
		
#contadores para as diagonais
soma_principal = 0
soma_secundaria = 0

#soma dos elementos da diagonal principal 
for i in range(N):
	for j in range(N):
		if(i == j):
			soma_principal = soma_principal + matriz[i,j]
			
#soma dos elemetos da diagonal secundaria			
for i in range(N):
	for j in range(N):
		if((i + j) == (N - 1)):
			soma_secundaria = soma_secundaria + matriz[i,j]

#diferenca entre os valores das diagonais
diferenca = soma_principal - soma_secundaria
print(diferenca)