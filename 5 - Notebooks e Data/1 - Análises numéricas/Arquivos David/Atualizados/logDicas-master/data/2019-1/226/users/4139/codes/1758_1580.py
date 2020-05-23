from numpy import*
nots = array(eval(input("notas: ")))
aluno = array(eval(input("nome aluno: ")))

i = 0
faltosos = 0
aprov = 0
reprov = 0
som = 0
while(i<size(nots)):
	if(nots[i] == -1):
		faltosos = faltosos + 1
	if(nots[i]>=6):
		aprov = aprov + 1
	if(nots[i]<6)and(nots[i]!=-1):
		reprov = reprov +1
	if(nots[i]>=0):
		som = som + nots[i]
	if(max(nots)==(nots[i])):
		top = aluno[i]
	i = i + 1

media = som/(size(nots) - faltosos)
print(faltosos)
print(aprov)
print(reprov)
print(round(media,2))
print(top)
