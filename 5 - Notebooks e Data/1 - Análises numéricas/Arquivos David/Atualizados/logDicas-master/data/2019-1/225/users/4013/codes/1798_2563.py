from numpy import*
vet = array(eval(input("primeiro vetor de notas:")))

while(size(vet) > 1):
	nmont = 0  
	for elemento in vet:
		if(elemento >= 5 and elemento < 7):
			nmont = nmont + 1
	
	print(nmont)
	
	vet = array(eval(input("vetor seguinte:")))