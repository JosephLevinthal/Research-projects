from numpy import*
from numpy.linalg import*
matriz=array(eval(input("Matriz de notas:")))
media=0
for i in range(shape(matriz)[1]):
	media=sum(matriz[i:2])
print(round(media,2))