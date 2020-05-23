from numpy import * 
nota = array(eval(input("nota:")))
nome = array(eval(input("aluno:")))
i=0
falt=0
apr=0
rep=0 
med=0
maior=0
while(i<size(nota)):
	if(nota[i]==-1):
	   falt=falt+1
	if((nota[i]>=6)and(nota[i]<=10)):
	   apr=apr+1
	if(nota[i]>-1 and nota[i]<6):
	   rep=rep+1
	if(nota[i]>-1):
		med=med+nota[i]
	if(nota[i]==max(nota)):
		maior = nome[i]
	i=i+1
print(falt)
print(apr)
print(rep)
print(round(med/(apr+rep),2))
print(maior)
