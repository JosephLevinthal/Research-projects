from numpy import*
from numpy.linalg import*
n= int(input("dimensao da matriz: "))
m=zeros((n,n), dtype=int)

for i in range(n):
	for j in range(n):
		if (i>j):
			m[i,j]=j+1
		elif(j>i):
			m[i,j]=i+1
		else:
			m[i,j]=i+1
print (m)
		