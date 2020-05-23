from numpy import * 

matricula= array(eval(input('matricula:')))
vet= zeros (2, dtype=int)
i=0
for i in range(size(matricula)):
	if(matricula[i] % 2 != 0):
		vet[i]= matricula[i]
	print(vet)