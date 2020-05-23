from numpy import*

vet = array(eval(input("vetor: ")))

#verificar se vai terminar
while(size(vet) > 1):
	i = 0
	
	for elemento in vet: 
		if(elemento >= 5) and (elemento < 7):
			i = i + 1
	print(i)
	
	vet = array(eval(input("proximo vetor:")))