from numpy import *
from numpy.linalg import *

matriz=array(eval(input("Notas: ")))

num=int(input("Num: "))

for i in range(shape(matriz)[1]):
	soma=sum(matriz[num,:])
	
media=soma/shape(matriz)[1]	

if(media>=5):
	print('PASSOU')
else:
	print('REPROVOU')
