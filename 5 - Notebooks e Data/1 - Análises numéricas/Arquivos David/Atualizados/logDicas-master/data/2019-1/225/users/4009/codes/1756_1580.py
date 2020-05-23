from numpy import*

notas= array(eval(input("Notas:")))
nomes= array(eval(input("Nomes dos alunos:")))

faltas=0
aprovacoes=0
presentes=0
reprovacoes=0
soma=0
n=0
aluno=""

i=0
while(i<size(notas)):
	if(notas[i]==-1):
		faltas=faltas+1
	if(notas[i]>=6):
		aprovacoes=aprovacoes+1
	if(notas[i]!=-1):
		presentes=presentes+1
		if(notas[i]<6):
			reprovacoes=reprovacoes+1
		soma=soma+notas[i]
		n=n+1
	if(notas[i]==max(notas)):
		aluno=nomes[i]
	i=i+1
	
print(faltas)
print(aprovacoes)
print(reprovacoes)
media= round(soma/n,2)
print(media)
print(aluno)