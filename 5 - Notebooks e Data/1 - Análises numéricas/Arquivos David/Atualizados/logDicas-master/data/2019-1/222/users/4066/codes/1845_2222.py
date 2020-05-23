from numpy import *

n = int(input("Dimensao: "))

dim = n - 1

matriz = zeros((n, n), dtype=int)

i = 0

while i < n:
	linha = array(eval(input("Linha: ")))
	matriz [i] = linha
	i = i + 1
	
soma_prin = 0
soma_sec = 0

for i in range(n):
	for j in range(n):
		if i == j:
			soma_prin = soma_prin + matriz[i, j]
			
		if (j == dim - i):
			soma_sec = soma_sec + matriz[i, j]

print(soma_prin - soma_sec)