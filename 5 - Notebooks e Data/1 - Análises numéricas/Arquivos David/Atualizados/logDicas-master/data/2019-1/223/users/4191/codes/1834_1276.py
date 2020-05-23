from numpy import *
from numpy.linalg import *

matriz=array(eval(input("Matriz: ")))
n=shape(matriz)[1]
vetor=zeros(n, dtype=int)

for i in range(size(n)):
	vetor[i]=sum(matriz[:,i])
	
x=1
for i in range(size(n)):
	if(vetor[i]==max(vetor)):
		x=i+1
		print(x)
		
