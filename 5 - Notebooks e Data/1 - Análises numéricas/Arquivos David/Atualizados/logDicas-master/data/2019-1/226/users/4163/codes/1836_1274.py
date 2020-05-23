from numpy import*
from numpy.linalg import*

n = int(input("digite um numero; "))
a = 0

new = zeros((n,n),dtype=int)
for i in range(n):
	for j in range(n):
		new[i,j] = min(i,j) + 1
		
print(new)
	