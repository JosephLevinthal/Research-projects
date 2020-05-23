from numpy import *

vet1 = array(eval(input("vetores: ")))
vet2 = array(eval(input("vetores2: ")))

i = 0
j = 0
faltosos = 0
aprovados = 0
reprovados = 0
s = 0
maior = max(vet1)

while(i < size(vet1)):
	if(vet1[i] == -1):
		faltosos = faltosos + 1
	elif(vet1[i] >= 6):
		aprovados = aprovados + 1
		s = s + vet1[i]
	elif(vet1[i] < 6 and vet1[i] >= 0):
		reprovados = reprovados + 1
		s = s + vet1[i]
		
	if(maior == vet1[i]):
		aluno = "" + vet2[i]
		
	i = i + 1
	
print(faltosos)
print(aprovados)
print(reprovados)
m = s / (aprovados + reprovados)
print(round(m, 2))
print(aluno)
		