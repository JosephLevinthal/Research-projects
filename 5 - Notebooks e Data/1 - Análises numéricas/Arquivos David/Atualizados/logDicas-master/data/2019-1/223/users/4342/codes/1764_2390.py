from numpy import * 
presentes = array(eval(input('presentes:')))
faltosos = array(eval(input('faltosos:')))

frequencia = (presentes - faltosos)
maior= 0
i= 0 
mes= 0 

while (i<12):
	if(frequencia[i] > maior):
		maior = frequencia[i]
		mes= i + 1
	i= i+1
	
print (mes)