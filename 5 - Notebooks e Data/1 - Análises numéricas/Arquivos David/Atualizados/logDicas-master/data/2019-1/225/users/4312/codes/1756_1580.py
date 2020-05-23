from numpy import*
notas = array(eval(input("Insira as notas: \n")))
alunos = array(eval(input("Insira o nome dos alunos: \n")))

i = 0
faltou = 0
aprovados = 0
reprovados = 0
media = 0
soma1 = 0
soma2 = 0

aux = 0

while(i < size(notas)):
	if(notas[i] == -1):
		faltou = faltou + 1
	elif(notas[i] >= 6):
		soma1 = soma1 + notas[i]
		aprovados = aprovados + 1
	elif(notas[i] != -1 and notas[i] < 6):
		soma2 = soma2 + notas[i]
		reprovados = reprovados + 1
	i = i + 1

while(notas[aux]!=max(notas)):
	aux = aux + 1 

media = (soma1+soma2)/(reprovados+aprovados)

print(faltou)
print(aprovados)
print(reprovados)
print(round(media, 2))
print(alunos[aux])

		
		