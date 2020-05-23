from numpy import*
from numpy.random import*
mat=array(eval(input("")))
#cria vetor de zeros no formato de inteiros
vet=zeros(mat.shape[0],dtype=int)
for i in range(mat.shape[0]):
	vet[i]=sum(mat[i,:])
#imprime o vetor	
print(vet)