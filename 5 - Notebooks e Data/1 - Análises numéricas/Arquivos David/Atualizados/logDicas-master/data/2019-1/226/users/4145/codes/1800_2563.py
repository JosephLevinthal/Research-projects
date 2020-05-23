from numpy import*
vet=array(eval(input("medias finais:")))
a=0
while(size(vet)>1):	
	a=a-a
	for i in vet:
		if((i>=5)and(i<7)):
			a=a+1
	
	print(a)
	vet=array(eval(input("medias finais:")))