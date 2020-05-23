from numpy import *
from numpy.linalg import *

matriz=array(eval(input("Matriz: ")))
n=shape(matriz)[0]
vetor=zeros(n, dtype=int)

for i in range(n):
	vetor[i]=sum(matriz[i,])
	
print(vetor)	
		