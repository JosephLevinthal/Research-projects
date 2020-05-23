from numpy import*

vet = array(eval(input("Primeiro vetor:")))

while (size(vet)>1):
	npar=0
	nimpar=0
	for elemento in vet:
		if (elemento%2==0):
		    npar= npar + 1
		else:
			nimpar= nimpar + 1
	print(npar)
	
	print(nimpar)
	
	print(size(vet))
	
	vet = array(eval(input("Primeiro vetor:")))

	
	