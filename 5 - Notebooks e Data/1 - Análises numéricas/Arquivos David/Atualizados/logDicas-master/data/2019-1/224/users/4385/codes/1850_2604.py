from numpy import*
from numpy.linalg import*
matriz = array(eval(input("dig a matriz: ")))
dcoluna = matriz.shape [1]
clinha = matriz.shape [0]
for i in range (clinha):
	print(max(matriz[i,:]))