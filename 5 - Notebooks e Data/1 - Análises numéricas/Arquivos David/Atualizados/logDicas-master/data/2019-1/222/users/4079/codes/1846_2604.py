from numpy import*
from numpy.random import*

matriz = array(dtype=float("Pagamentos: "))
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]

for i in range(linhas):
	print(max(matriz[i,:]))