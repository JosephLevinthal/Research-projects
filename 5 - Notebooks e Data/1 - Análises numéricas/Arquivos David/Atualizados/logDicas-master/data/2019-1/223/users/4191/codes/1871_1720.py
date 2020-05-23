from numpy import *
from numpy.linalg import *

matriz=array(eval(input("Notas:")))
notas=shape(matriz)[1]
aprovado=0

for i in range(shape(matriz)[0]):
	soma=sum(matriz[i,:])
	media=soma/notas
		
	if(media>=5):
		aprovado=aprovado+1

total=aprovado/shape(matriz)[0]*100			
print(round(total,2))