from numpy import*
from numpy.linalg import*
n = int(input("numero inteiro: "))
m = ones((n,n))
g = -1
for x in range(n):
	g= g+1
	for y in range(n):
		m[,y]=m[,y]+g
		
print(m)

	
