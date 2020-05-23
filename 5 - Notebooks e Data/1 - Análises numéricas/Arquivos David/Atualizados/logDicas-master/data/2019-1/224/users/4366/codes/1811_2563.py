from numpy import*
vet=array(eval(input("Primeiro vetor: ")))
ap=0
while(size(vet)>1):
	for i in vet:
		if(i>=5) and (i<7):
			ap=ap+1
	print(ap)
	ap = 0
	vet=array(eval(input("Primeiro vetor: ")))
	
	