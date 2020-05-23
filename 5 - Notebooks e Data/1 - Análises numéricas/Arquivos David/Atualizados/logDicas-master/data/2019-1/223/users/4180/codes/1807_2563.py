from numpy import*

vet = array(eval(input("Medias finais: ")))

while(size(vet)>1):
	
	aprov = 0
	
	for elemento in vet:
		if (5 <= elemento < 7):
			aprov = aprov + 1
		
	print(aprov)
		
	vet = array(eval(input("Proximo vetor:")))
	
	
	

