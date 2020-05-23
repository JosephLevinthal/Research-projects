from numpy import *

nota=array(eval(input("Notas: ")))

nome=array(eval(input("Nomes: ")))


cont=0
faltaram=0
aprovados=0
reprovados=0
soma=nota[cont]
vetor= zeros(size(nota))
i=0
maior=""

while(cont<size(nota)):
	if(nota[cont]>=6 and nota[cont]<=10):
		aprovados=aprovados+1
	
	elif(nota[cont]==-1):
		faltaram=faltaram+1
	
	elif(nota[cont]<6 and nota[cont]>=0):	
		reprovados=reprovados+1
	
	elif(nota[cont]>=0 and nota[cont]<=10):
		soma=soma+soma
	
	elif(max(nota)==nota[i]):
		maior=nome[i]
	
	cont=cont+1	

	i=i+1

media=soma/aprovados+reprovados

print(faltaram)
print(aprovados)
print(reprovados)

print(round(media, 2))
print(maior)
