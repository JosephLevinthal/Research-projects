from numpy import*
vet = array(eval(input("primeiro vetor: ")))

while(size(vet)>1):
	npar = 0
	impar = 0
	for i in range(size(vet)):
		if (vet[i] % 2 == 0):
			npar = npar + 1
		else:
			impar = impar + 1
		
	print(npar)
		
	print(impar)
			
	print(size(vet))

	vet = array(eval(input("segundo vetor: ")))
