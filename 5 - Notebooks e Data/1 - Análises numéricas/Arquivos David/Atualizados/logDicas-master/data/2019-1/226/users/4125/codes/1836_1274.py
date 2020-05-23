from numpy import*
from numpy.linalg import*
n = int(input("digite um numero n natural: "))
n1 = zeros([n,n], dtype = int)
for i in range(n):
	for j in range(n):
		if(i<=j):
			n1[i,j] = i + 1
		elif(i>j):
			n1[i,j] = j + 1
print(n1)