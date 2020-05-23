from numpy import * 

nf= array(eval(input('numero de faltas:')))
vet= zeros(6, dtype=float)

for i in range(size(nf)):
	if(nf[i]==2):
		vet[0]= vet[0] + 1
	elif( nf[i]==3):
		vet[1]= vet[1] + 1
	elif(nf[i]==4):
		vet[2]= vet[2] + 1
	elif(nf[i]==5):
		vet[3]= vet[3] + 1
	elif(nf[i]==6):
		vet[4]= vet[4] + 1
	elif(nf[i]==7):
		vet[5]= vet[5] + 1

total = sum(vet)		
for i in range(size(vet)):
	
	vet[i]=round(((vet[i]/total)*100), 1)
print(vet)
	
	