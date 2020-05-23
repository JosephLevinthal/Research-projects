from numpy import* 
notas = array(eval(input("notas:")))
alunos = array(eval(input("alunos:")))


faltou = 0
aprovados = 0
reprovados = 0
soma_das_anotas = 0
i = 0

while(i < size(notas)):
	if(notas[i] == -1):
		faltou = faltou + 1
		
	if(notas[i] >= 6 and notas[i] <= 10 ):
		aprovados = aprovados + 1
		soma_das_anotas = soma_das_anotas + notas[i]
		
	if(notas[i] >= 0 and notas[i] < 6):
		reprovados = reprovados + 1
		soma_das_anotas = soma_das_anotas + notas[i]
		
	if(notas[i] == max(notas)):
		maior_nota = alunos[i]
		
	i = i + 1
	
alunos_Presentes = reprovados + aprovados
media = soma_das_anotas/alunos_Presentes

print(faltou)
print(aprovados)
print(reprovados)
print(round((media),2))
print(maior_nota)