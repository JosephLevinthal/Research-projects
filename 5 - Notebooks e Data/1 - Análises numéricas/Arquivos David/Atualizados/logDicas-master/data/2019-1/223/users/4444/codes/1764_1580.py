from numpy import *
notas=array(eval(input('Digite a notas do aluno:  ')))
nome=array(eval(input('Digite o nome do aluno:')))
qdt_faltantes=0
presentes=0
aprovado=0
reprovado=0
i=0
soma=0
qdt_validas=0
maximo=0
i_maximo=0

while(i<len(notas)):
	
	if(notas[i]==-1):
		qdt_faltantes = qdt_faltantes+1
	
	if(6 <= notas[i] <= 10):
		aprovado=aprovado +1
		
	if(0<=notas[i]<6):
		reprovado= reprovado +1
		
	if(notas[i]!= -1):
		soma=soma + notas[i]
		qdt_validas=qdt_validas + 1
	if(notas[i]>maximo):
		maximo=notas[i]
		i_maximo=i
		
		
	i=i+1
print(qdt_faltantes)
print(aprovado)
print(reprovado)
print(round(soma/qdt_validas,2))
print(nome[i_maximo])




	
	
	

	