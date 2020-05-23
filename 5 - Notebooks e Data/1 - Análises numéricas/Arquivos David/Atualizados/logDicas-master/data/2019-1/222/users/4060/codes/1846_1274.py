from numpy import *
from numpy.linalg import *

matriz=int(input("numero: "))
zeros=zeros((matriz,matriz), dtype=int)

for i in range(matriz):
	for j in range(matriz):
		if (i<j):
			zeros[i,j]=i+1
		elif(j<i):
			zeros[i,j]=j+1
		elif(i==j):
			zeros[i,j]=j+1

print(zeros)