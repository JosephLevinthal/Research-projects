from numpy import *

numero = int(input("Numero: "))
matriz_nula = zeros((numero, numero), dtype=int)

# Atribuindo os elementos na matriz nula
# Note que se i > j, então M(i, j) = j + 1
# e se i <= j, então M(i, j) = i + 1

for i in range(numero):
	for j in range(numero):
		if i > j:
			matriz_nula[i, j] = j+1
		elif i <= j:
			matriz_nula[i, j] = i+1
	
print(matriz_nula)