from numpy import *

notas = array(eval(input("Digite ")))
nomes =  array(eval(input("Digite ")))

faltas = 0
aprovacoes = 0
presentes = 0
reprovacoes = 0
soma = 0
n = 0
aluno = 0

i = 0
while (i < size(notas)):
	if (notas[i] == -1):
		faltas += 1
	if (notas[i] >= 6):
		aprovacoes += 1
	if (notas[i] != -1):
		presentes += 1
		if (notas[i] < 6):
			reprovacoes += 1
		soma += notas[i]
		n += 1
	if (notas[i] == max(notas)):
		aluno = nomes[i]
	i += 1

print(faltas)
print(aprovacoes)
print(reprovacoes)
media = round(soma/n, 2)
print(media)
print(aluno)