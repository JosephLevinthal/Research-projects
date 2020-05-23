from numpy import *
from numpy.linalg import *

n=int(input("Numero inteiro: "))

matriz=zeros((n,n), dtype=int)

for i in range (n):	
	for j in range(n):
		matriz[i,j]=min(i,j)+1
		
print(matriz)		
