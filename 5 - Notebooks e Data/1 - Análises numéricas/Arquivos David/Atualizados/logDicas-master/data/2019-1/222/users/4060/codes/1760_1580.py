from numpy import*
notas=array(eval(input("notas obtidas: ")))
nome=array(eval(input("nome dos alunos: ")))
cont=0
falta=0
aprov=0
rep=0
pres=0
i=0 #para achar o indice da maior nota e procurar o nome referente a ele 
while(cont < size(notas)):
	if(notas[cont]==-1):
		falta=falta+1
	elif(notas[cont]>=6):
		aprov=aprov+1
		pres=pres+notas[cont] #tambem se conta para tirar a media
	elif(notas[cont]<6):
		rep=rep+1
		pres=pres+notas[cont] #tambem se conta para tirar a media
	elif(notas[cont]>=0):
		pres=pres+notas[cont] #se conta para tirar a media
	cont=cont+1
while(notas[i]!=max(notas)):
	i=i+1
print(falta)	
print(aprov)
print(rep)
print(round(pres/(aprov+rep), 2))
print(nome[i])
