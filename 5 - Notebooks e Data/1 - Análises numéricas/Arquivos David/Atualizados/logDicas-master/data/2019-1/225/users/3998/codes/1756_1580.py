from numpy import*

v1 = array(eval(input()))
v2 = array(eval(input()))

i = 0
j = 0
faltosos = 0
aprovados = 0
reprovados = 0
s = 0
maior = max(v1)

while(i < size(v1)):
	if(v1[i] == -1):
		faltosos = faltosos + 1
	elif(v1[i] >= 6):
		aprovados = aprovados + 1
		s = s + v1[i]
	elif(v1[i] < 6 and v1[i] >= 0):
		reprovados = reprovados + 1
		s = s + v1[i]

	if(maior == v1[i]):
		aluno = "" + v2[i]
	
	i = i + 1

print(faltosos)
print(aprovados)
print(reprovados)
m = s / (aprovados + reprovados)
print(round(m, 2))
print(aluno)