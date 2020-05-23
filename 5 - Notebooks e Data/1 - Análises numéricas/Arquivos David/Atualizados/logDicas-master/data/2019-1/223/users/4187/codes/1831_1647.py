from numpy import*
percentual = array(eval(input("percentual de presenca:")))

aprovados = 0

for i in range(size(percentual)):
	if(percentual[i] >= 70 ):
		aprovados = aprovados + 1
print(aprovados)		
alunos_aprovados = zeros(aprovados, dtype=int)

i_2 = 0
for i in range(0,size(percentual)):
	if(percentual[i] >= 70):
		if(i_2 < size(percentual)):
			alunos_aprovados[i_2] = i 
			i_2 = i_2 + 1
	
print(alunos_aprovados)