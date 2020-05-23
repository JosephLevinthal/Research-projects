from numpy import *
from numpy.linalg import *

tabela = array([[0,2,2,2,0],
						[2,5,8,5,2],
						[2,8,16,8,2],
						[2,8,16,8,2],
						[2,5,8,5,2],
						[0,2,2,2,0]
					  ])

e1 = int(input("Valor 1: "))
e2 = int(input("Valor 2: "))

matriz = zeros((5,5),dtype=int)

i = e1
j = e2

print(tabela[i,j])

#for i in range(0,tabela):
#	for j in range(0,tabela):
#		print(matriz[i,j])

#print(tabela)