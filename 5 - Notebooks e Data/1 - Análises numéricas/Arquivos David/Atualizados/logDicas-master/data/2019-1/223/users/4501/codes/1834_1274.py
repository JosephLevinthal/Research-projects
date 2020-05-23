from numpy import*
from numpy.linalg import*
N=int(input("n: "))
a=zeros((N,N), dtype=int)
for i in range(N):
	for j in range(N):
		a[i,j]=min(i,j)+ 1
print(a)			