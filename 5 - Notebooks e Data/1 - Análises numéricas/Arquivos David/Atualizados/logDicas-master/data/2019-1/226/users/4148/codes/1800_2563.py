from numpy import*

vet = array(eval(input("medias: ")))


while (size(vet)>1):
	
	n=0

	for x in vet:
		if(x>=5 and x< 7):
			n = n + 1
			
	print(n)    
	
	vet = array(eval(input("medias: ")))
	