from numpy import*
from numpy.linalg import*

matriz=array(eval(input("")))
s=matriz.shape[0]
vetor=zeros(s,dtype=int)
for i in range(s):
	for j in range(s):
		vetor[i,j]=sorted(matriz,reverse=True)
print(vetor)