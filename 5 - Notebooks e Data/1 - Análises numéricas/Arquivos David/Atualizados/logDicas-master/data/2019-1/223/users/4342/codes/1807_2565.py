from numpy import *

media= array(eval(input('media alunos:')))
nhoras = array(eval(input('numero de horas:')))
carga = array(eval(input('carga horaria:')))
vet= zeros(3, dtype=int)
 
for i in range (size(media)):
	if ((media[i])>= 5 and (nhoras[i])>= (carga*0.75)):
		vet[0]=vet[0] + 1
	elif((media[i]) <5 and (nhoras[i])>= (carga*0.75)):
		vet[1]= vet[1] + 1
	elif((nhoras[i]) < (carga*0.75)):
		vet[2]= vet[2]+ 1
print(vet)
			