from numpy import*
vet = array(eval(input("Primeiro vetor: ")))
while(len(vet)>1):
	npar = 0;
	nimpar = 0;
	for i in vet:
		if i%2==0:
			npar+=1
		else:
			nimpar+=1
	print(npar)
	print(nimpar)
	print(len(vet))
	vet = array(eval(input(" "))