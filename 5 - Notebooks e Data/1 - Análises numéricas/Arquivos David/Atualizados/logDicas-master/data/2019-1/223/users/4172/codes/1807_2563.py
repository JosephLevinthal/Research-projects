from numpy import*

vet=array(eval(input("")))

while(size(vet)>1):
	o=0
	for l in  vet:
		if(l>=5 and l<7):
			o+=1
	print(o)
	vet=array(eval(input("")))
	