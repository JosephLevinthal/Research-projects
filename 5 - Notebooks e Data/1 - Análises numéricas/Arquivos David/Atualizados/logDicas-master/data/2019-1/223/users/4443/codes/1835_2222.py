from numpy import *
from numpy.linalg import *
ordem = array(eval(input("Digite a ordem da matriz: "))) #ordem da matriz
#criacao da estrutura da matriz para a ordem dada
mat = zeros((ordem, ordem))
for i in range(ordem): #preenchimento das posicoes (aij) da matriz conforme os numeros sao digitados um a um
	for j in range(ordem):
		valor = int(input("Digite um valor para uma posicao matriz: "))
		mat[i,j] = valor
#soma dos valores da diagona principal		
principal = 0
for i in range(ordem):
	for j in range(ordem):
		if(i == j):
			principal = principal + mat[i,j]
#invertendo a posicao das colunas dentro da matriz para transformar a diaginal secundaria em principal
aux = zeros((ordem, 1))
for i in range(ordem//2):
	aux[:,0] = mat[:,i]
	mat[:,i] = mat[:, -1-i]
	mat[:, -1-i] = aux[:,0]
#soma dos valores da diagnoal principal da nova matriz (igual a secundaria da matriz original)
secundaria = 0
for i in range(ordem):
	for j in range(ordem):
		if(i == j):
			secundaria = secundaria + mat[i,j]
dif = int(principal - secundaria)
print(dif)		