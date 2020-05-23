from numpy import *

matriz = array(eval(input("Pagamentos: ")))
linhas = shape(matriz)[0]

for i in range(linhas):
	print(max(matriz[i, :]))#dar as saidas dos valores maximos
	
	