from numpy import*
vet = array(eval(input("Digite o vetor: ")))


while(size(vet)>1):
	n=0
	for element in vet:
		if(element<7 and element>=5):
			n = n+1
	print(n)
	vet = array(eval(input("Digite o vetor: ")))

			
	
	