from numpy import *

gols = array(eval(input("gols feitos:")))
sgols = array(eval(input("gols sofridos:")))
vet = zeros(3, dtype=int)
soma= 0 
for i in range(size(gols)):
	if( gols[i] > sgols[i] ):
		vet[0]= vet[0] + 1
	elif( gols[i] == sgols[i]):
		vet[1]= vet[1] + 1
	elif( gols[i] < sgols[i]):
		vet[2]= vet[2] + 1
		
print(vet)	