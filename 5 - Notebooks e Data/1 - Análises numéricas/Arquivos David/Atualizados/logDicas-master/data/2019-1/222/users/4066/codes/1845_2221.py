from numpy import *

matriz = array(eval(input("Notas: ")))
linhas = shape(matriz)[0]
colunas = shape(matriz)[1]

soma = 0


for i in range(linhas):
	menor_nota = min(matriz[i, :])
	soma = soma + menor_nota
	
media = round(soma/linhas, 2)
print(media)