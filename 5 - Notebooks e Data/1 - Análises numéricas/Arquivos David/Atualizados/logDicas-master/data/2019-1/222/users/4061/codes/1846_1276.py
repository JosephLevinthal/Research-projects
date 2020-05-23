from numpy import*

matriz = array(eval(input("Digite: ")), dtype=int)
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]

vetor_nulo = zeros(7, dtype=int)

for i in range(colunas):
	
	# Soma das colunas da matriz sendo atribuida ao vetor nulo
		
	vetor_nulo[i] = sum(matriz[:,i])

# Verificando qual o dia que mais funcionários trabalham
# Sendo 1 = domingo, 2 = segunda, ..., 7 = sábado

for p in range(colunas):
	if vetor_nulo[p] == max(vetor_nulo):
		print(p+1)