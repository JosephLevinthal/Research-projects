from numpy import*

nota = array(eval(input("nota:")))
aluno = array(eval(input("aluno:")))

faltaram = 0
aprovados = 0
reprovados = 0
mp = 0 # media de presentes
i = 0

while(i < size(nota)):
	if ( nota[i] == -1):
		faltaram = faltaram + 1
		
	
	if( 6 <= nota[i] <= 10 ):
		aprovados = aprovados + 1
		mp = mp + nota[i]
		
	if (0 <= nota[i] < 6):
		reprovados = reprovados + 1
		mp = mp + nota[i]	
	
	if (nota[i] == max(nota)):
		maiornota = aluno[i]
	i = i + 1	
	
alunosp = aprovados + reprovados
media = mp/ alunosp

print(faltaram)
print(aprovados)
print(reprovados)
print(round(media,2))
print(maiornota)
	

	
	