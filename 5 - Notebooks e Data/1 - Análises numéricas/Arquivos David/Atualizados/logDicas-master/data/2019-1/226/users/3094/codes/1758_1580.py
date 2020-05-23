from numpy import *

notas = array(eval(input("")))
alunos = array(eval(input("")))

i = 0
faltaram = 0
passaram = 0
reprovaram = 0
soma = 0
maior = 0

while(i < size(notas)):
	if(notas[i] == -1.0):
		faltaram = faltaram + 1
	elif (notas[i] >= 6.0):
		passaram = passaram + 1
	elif(notas[i] < 6.0 and notas[i] != -1):
		reprovaram = reprovaram + 1
	if(notas[i] != -1 ):
		soma = soma + notas[i]
	if(notas[i] == max(notas)):
		maior = 1
	i = i + 1
print(faltaram)
print(passaram)
print(reprovaram)
print(round(soma / (size(notas) -  faltaram ),2))
print(alunos [maior])





