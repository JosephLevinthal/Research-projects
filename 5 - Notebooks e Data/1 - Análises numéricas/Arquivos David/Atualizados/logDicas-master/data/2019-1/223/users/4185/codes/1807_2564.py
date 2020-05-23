from numpy import*
vet1= array(eval(input("digite o valor: ")))
vet2= array(eval(input("digite o valor: ")))
vet3= array(zeros(3,dtype=int))

for i in range(size(vet1)):
	if (vet1[i] > vet2[i]):
		vet3[0] = vet3[0] + 1 
	elif (vet1[i] == vet2[i]):
		vet3[1] = vet3[1] + 1
	elif (vet1[i] < vet2[i]):
		vet3[2] = vet3[2] + 1
		
print(vet3)
	

