from numpy import*

vet1 = array(eval(input("vetor1:")))
vet2 = array(eval(input("vetor2:")))
vetn = zeros(3, dtype=int)

for elemento in range(size(vet1)):
	if(vet1[elemento] > vet2[elemento]):
		vetn[0] = vetn[0] + 1
	elif(vet1[elemento] == vet2[elemento]):
		vetn[1] = vetn[1] + 1
	elif(vet1[elemento] < vet2[elemento]):
		vetn[2] = vetn[2] + 1
print(vetn)
		
	

