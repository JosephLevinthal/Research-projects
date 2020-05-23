from numpy import *

peso= array(eval(input('peso:')))
altura= array(eval(input('altura:')))
vet= zeros(3, dtype=float)

for i in range(size(peso)):
	if(peso[i]>=0 and altura[i]>=0)	:
		vet[0]=round(peso[0]/(altura[0]**2), 2)
	if(peso[i]>=0 and altura[i]>=0)	:
		vet[1]=round(peso[1]/(altura[1]**2),2)
	if(peso[i]>=0 and altura[i]>=0)	:
		vet[2]=round(peso[2]/(altura[2]**2),2)

imc= (peso[i]/(altura[i]**2))
print(vet)
print('O MAIOR IMC DA TURMA EH:',max(imc))