from numpy import*
from numpy.linalg import* 

n = int(input("numero:"))
y = zeros((n,n),dtype=int)

for i in range(n):
	for j in range(n):
		y[i,j] =  min(i,j) + 1
	
print(y)
