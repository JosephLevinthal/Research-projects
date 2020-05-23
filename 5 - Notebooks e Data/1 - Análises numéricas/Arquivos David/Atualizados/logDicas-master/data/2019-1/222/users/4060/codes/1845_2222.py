from numpy import *
from numpy.linalg import *
n=int(input("Insira a ordem da matriz: "))
for i in range(n):
	m=input("Insira uma matriz quadrada: ")
dp=0
ds=0
for i in range(n):
	for j in range(n):
		if (i==j):
			dp=dp+m[i,j]
for i in range(n):
	for j in range(n):	
		if((i+j)==(n-1)):
			ds=ds+m[i,j]
			
print(dp-ds)
	
