from numpy import *
from numpy.linalg import *
b=array(eval(input("digite:")))
tamanho=shape(b)[0]
result=zeros(tamanho, dtype=int)

for i in range(tamanho):
	result[i]=sum(b[i,:])
print(result)
	
	