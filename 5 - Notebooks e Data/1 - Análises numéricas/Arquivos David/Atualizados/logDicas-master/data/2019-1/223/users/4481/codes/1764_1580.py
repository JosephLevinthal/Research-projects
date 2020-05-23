from numpy import *

notas = array(eval(input("Digite as notas dos estudantes: ")))
estudantes = array(eval(input("Digite os nomes dos estudantes: ")))

faltas = 0
aprovados = 0
reprovados = 0
soma = 0
nome = "a"
i = 0

while(i < size(notas)):
	if(notas[i] == -1):
		faltas = faltas +1
	if(6 <= notas[i] <= 10):
		aprovados = aprovados +1
		soma = soma + notas[i]
	if(0 <= notas[i] < 6):
		reprovados = reprovados +1
		soma = soma + notas[i]
	if(notas[i] == max(notas)):
		nome = estudantes[i]
	i = i+1    

total = aprovados + reprovados
media = soma/total

print(faltas)
print(aprovados)
print(reprovados)
print(round(media, 2))
print(nome)