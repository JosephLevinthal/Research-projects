from numpy import *
from numpy.linalg import *
N=int(input("numero: "))
matrizero=zeros((N,N),dtype=int)
for i in range(N):
	for j in range (i,N):
		matrizero[i,j]=i+1
		matrizero[j,i]=i+1
print(matrizero)