from numpy import *
from numpy.linalg import *
number=int(input("digite um numero: "))
matriz=zeros((number,number),dtype=int)
for i in range(number):
	for j in range(i,number):
		matriz[i,j]=i+1
		matriz[j,i]=i+1
print(matriz)
