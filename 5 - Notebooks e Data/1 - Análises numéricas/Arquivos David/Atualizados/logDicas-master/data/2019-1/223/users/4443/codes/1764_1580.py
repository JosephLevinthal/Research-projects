from numpy import *
notas = array(eval(input("Digite as notas dos estudantes: "))) #vetor de entrada dos valores das notas
estudantes = array(eval(input("Digite os nomes dos estudantes: "))) #vetor de entrada dos valores das nomes dos estundates

faltas = 0 #contador do numero de faltas
aprovados = 0  #contador do numero de estudantes com nota igual ou superior a 6
reprovados = 0 #contador do numero de estudantes com nota inferior a 6
soma = 0 #variavel acumuladora das notas
nome = "a" #vetor contendo um valor arbitrario que sera substituido depois
i = 0 #variavel contadora do laco

while(i < size(notas)): #condicao do laco, i percorre todas as posicoes do vetor de entrada
	if(notas[i] == -1): #testa a condicao para faltas
		faltas = faltas +1 #se verdade, incrementa o numero de faltas
	if(6 <= notas[i] <= 10): #testa a condicao de aprovados
		aprovados = aprovados +1 #se verdade, incrementa o numero de aprovados
		soma = soma + notas[i] #incrementa a variavel acumuladora das notas
	if(0 <= notas[i] < 6): #testa a condicao de reprovados
		reprovados = reprovados +1 #se verdade, incrementa o numero de reprovados
		soma = soma + notas[i] #incrementa a variavel acumuladora das notas
	if(notas[i] == max(notas)): #busca a maior nota no vetor nota
		nome = estudantes[i] #busca o nome do estudante no mesmo indici i do vetor notas e atualiza a variavel nome
	i = i+1	#incrementa o laco

total = aprovados + reprovados #total dos estudantes que compareceram
media = soma/total #definicao da media
#impressao de todas as variaveis solicitadas
print(faltas)
print(aprovados)
print(reprovados)
print(round(media, 2))
print(nome)
	