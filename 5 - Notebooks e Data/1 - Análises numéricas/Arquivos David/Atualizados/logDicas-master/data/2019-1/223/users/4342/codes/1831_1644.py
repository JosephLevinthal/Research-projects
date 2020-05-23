from numpy import*

nota= array(eval(input('notas dos alunos:')))
soma=0

for i in range(size(nota)):
	if(nota[i] < 5):
		soma= soma +1
print(soma)

vet= zeros(soma, dtype=int)
j= 0
for i in range(size(nota)):	
	if(nota[i]<5):
		vet[j]= i
		j= j +1 
print(vet)



	