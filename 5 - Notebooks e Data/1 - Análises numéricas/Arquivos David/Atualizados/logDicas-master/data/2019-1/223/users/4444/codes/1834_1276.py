from numpy import *
# Leitura da matriz 'quadro'
from numpy import *
from numpy.linalg import *
b=array(eval(input("digite:")))
tamanho=shape(b)[1]
result=zeros(tamanho, dtype=int)

for j in range(tamanho):
	result[j]=sum(b[:,j])
maior=max(result)
for i in range(tamanho):
	if result[i]==maior:
		print(i+1)
		
	
	