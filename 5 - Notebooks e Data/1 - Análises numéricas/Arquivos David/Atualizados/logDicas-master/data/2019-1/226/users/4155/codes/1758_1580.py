from numpy import *
nota = array(eval(input("notas: ")))
aluno = array(eval(input("alunos: ")))

aprov = 0
faltaram = 0
reprov = 0
presentes = 0
medpres = 0
i = 0

while(i < size(nota)):
	if(nota[i] == -1):
		faltaram = faltaram + 1
		
	if(nota[i] >= 6 and nota[i] <= 10):
		aprov = aprov + 1
		medpres = medpres + nota[i]
		
	if(nota[i] < 6 and nota[i] >= 0):
		reprov = reprov + 1
		medpres = medpres + nota[i]
		
	if(nota[i] == max(nota)):
		maior_nota = aluno[i]
	i = i + 1

alunop = reprov + aprov
media = medpres/alunop

print(faltaram)
print(aprov)
print(reprov)
print(round((media),2))
print(maior_nota)
	
