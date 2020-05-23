from numpy import *
nota = array(eval(input("digite as notas: ")))
alunos = array(eval(input("digite os nomes dos alunos ")))
i = 0
faltas = 0
aprovados = 0
reprovados = 0
soma = 0
media = 0
maior = 0
while(i<size(nota)):
	if(nota[i]==-1):
		faltas = faltas + 1
	elif(nota[i]>=6):
		aprovados = aprovados + 1
	elif(nota[i]>=0 and nota[i]<6):
		reprovados = reprovados + 1
	if(nota[i] != -1):
		soma = soma + nota[i]
	if(nota[i] == max(nota)):
		maior = i
	i = i + 1
a = soma/(size(alunos)-faltas)
print(faltas)
print(aprovados)
print(reprovados)
print(round(a,2))
print(alunos[maior])