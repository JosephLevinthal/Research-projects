from numpy import *
v = array(eval(input("")))
aluno = array(eval(input("")))
i = 0
faltante = 0
aprovados = 0
reprovados = 0
media = 0.0
n= 0
maior = 0
while(i<len(v)):
	if(v[i]==-1):
		faltante+=1
	else:
		media+=v[i]
		n+=1
	if(v[i]>=6):
		aprovados+=1
	if(v[i]<6 and v[i]>-1):
		reprovados+=1
	
	if(v[maior]<v[i]):
		maior = i
	i+=1
	for i
print(faltante)
print(aprovados)
print(reprovados)
print(round(media/n,2))
print(aluno[maior])