from numpy import*
vet1 = array(eval(input("Gols do time: ")))
vet2 = array(eval(input("Gols do adversario:")))
vcont = zeros(3, dtype=int)
for i in range (0, size(vet1)):
	if (vet1[i] > vet2[i]):
		vcont[0] = vcont[0] + 1
	elif (vet1[i] == vet2[i]):
		vcont[1] = vcont[1] + 1
	else:
		vcont[2] = vcont[2] + 1
print(vcont)

