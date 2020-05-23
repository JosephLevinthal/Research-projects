from numpy import *
from numpy.linalg import *
from math import *
matriz=array(eval(input()), dtype=float)
n=shape(matriz)[0]
t=n*n-n
k=0
z=zeros(t, dtype=float)
for i in range(n):
	for j in range (n):
		if ((i+j)!=(n-1)):
			z[k]=matriz[i,j]
			k=k+1
print(min(z))
			