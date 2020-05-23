from numpy import *
vet=array(eval(input("Gols feitos: ")))
vet2=array(eval(input("Gols sofridos: ")))
vitoria=0
derrota=0
empate=0

for i in range(size(vet)):
	if(vet[i]>vet2[i]):
		vitoria=vitoria+1
	elif(vet[i]<vet2[i]):
		derrota=derrota+1
	elif(vet[i]==vet2[i]):
		empate=empate+1

vet3=zeros(3, dtype=int)

vet3[0]=vitoria
vet3[1]=empate
vet3[2]=derrota

print(vet3)
		

