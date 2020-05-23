from numpy import *
vet1 = array(eval(input("Vetor de gols do seu time: ")))
vet2 = array(eval(input("Vetor de gols do time adversario: ")))
soma1 = 0
soma2 = 0
soma3 = 0
vet3 = zeros(3, dtype=int)
for i in range(size(vet1)):
	if (vet1[i] > vet2[i]):
		soma1 = soma1 + 1
	elif (vet1[i] == vet2[i]):
		soma2 = soma2 + 1
	elif (vet1[i] < vet2[i]):
		soma3 = soma3 + 1
vet3[0] = soma1
vet3[1] = soma2
vet3[2] = soma3
print(vet3)
