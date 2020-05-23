from numpy import*
from numpy.linalg import*
n=int(input(""))

vet=zeros((n,n),dtype=int)


for j in range(n):
	for i in range(n):
		vet[i,j]=min(i,j)+1
print(vet)