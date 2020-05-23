from numpy import *
vet = array(eval(input("Primeiro vetor: ")))
while(size(vet) > 1):
	par = 0
	impar = 0
	for x in vet:
		if (x % 2 == 0):
			par = par + 1
		else: 
			impar = impar + 1
	print(par)
	print(impar)
	print(size(vet))
	vet = array(eval(input("Proximo vetor: ")))