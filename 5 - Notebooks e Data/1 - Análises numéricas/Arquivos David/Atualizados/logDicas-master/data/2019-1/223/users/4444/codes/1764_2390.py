from numpy import *
presentes = array(eval(input('Digite presentes:')))
ausentes = array(eval(input('Digite ausentes:')))
frequencia = presentes - ausentes
mes = array([1,2,3,4,5,6,7,8,9,10,11,12])
i = 0
while(frequencia[i] != max(frequencia)):
	i = i+1
print(mes[i])
