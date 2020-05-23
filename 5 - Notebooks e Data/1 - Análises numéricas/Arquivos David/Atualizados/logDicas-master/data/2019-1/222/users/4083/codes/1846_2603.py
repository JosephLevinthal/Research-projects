from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite a matriz: ")))

linhas = shape(v)[0]
colunas = shape(v)[1]
matriz = zeros((linhas, colunas), dtype= int)
vetor = zeros(colunas, dtype=int)

for i in range(colunas):
	for j in range(linhas):
		vetor[j] = v[j,i]
		
	vetor = sorted(vetor,reverse=True)
	matriz[:,i] = vetor
	
print(matriz)