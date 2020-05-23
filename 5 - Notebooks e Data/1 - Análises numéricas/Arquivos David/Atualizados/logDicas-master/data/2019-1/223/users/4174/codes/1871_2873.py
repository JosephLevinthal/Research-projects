from numpy import*
from numpy.linalg import*

matriz = array(eval(input("matriz: ")))
ma = 0

for i in range(shape(matriz)[0]):
	ma = ma + matriz[i,0] * matriz[i,1]
media = ma / (shape(matriz)[0])

print(round(media,2))	