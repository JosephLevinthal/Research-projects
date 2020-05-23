from numpy import *

matriz = array(eval(input("Pagamentos: ")))
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]

for i in range(linhas):
	print(sum(min(matriz[i, :]/size(matriz))))