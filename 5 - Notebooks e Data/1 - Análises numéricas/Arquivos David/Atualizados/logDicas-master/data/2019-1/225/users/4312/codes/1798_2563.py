from numpy import*
vet = array(eval(input("Vetor: ")))

while(size(vet) > 1):

	x = 0
	
	for i in range(size(vet)):
		if(vet[i] >= 5 and vet[i] < 7):
			x = x + 1
	
	print(x)
	
	vet = array(eval(input("Insira um novo vetor: ")))
			
			