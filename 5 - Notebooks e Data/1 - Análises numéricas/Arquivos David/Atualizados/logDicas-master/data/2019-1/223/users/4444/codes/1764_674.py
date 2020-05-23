# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 

from numpy import *
notas= array(eval(input('digite um numeoro inteiro: ')))
compras=0
i=0
while(i > len(notas)):
	if(notas[i] > 80):
		notas[i] = notas[i]- 5
	else:
		notas[i]=notas[i]
		compras=compras+ notas[i]
i=i+1
print(round(compras,2))
		


print(size(notas)) #imprime o tamanho do vetor 
print(notas[0]) #imprime o primeiro elemento do vetor
print(notas[-1])  #imprime o ultimo elemento do vetor
print(max(notas)) #imprime o maior elemento do vetor
print(min(notas)) # imprime o menor elemento do vetor
print(sum(notas)) # imprime a soma de todos os elementos do vetor
print(round(sum(notas)/len(notas),2)) #imprime a media dos elementos do vetor