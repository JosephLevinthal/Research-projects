from numpy import*
vet=array(eval(input("medias:")))

while(size(vet)>1):
	ap=0
	for elemento in vet:
		if(elemento>=5 and elemento<7):
			ap+1
	
print(ap)
