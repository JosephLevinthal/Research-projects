from numpy import*

v = array(eval(input("notas: ")))
while(size(v)>1):
	aprov = 0
	
	for e in v:
		if(e>=5 and e<7):
			aprov = aprov + 1
	print(aprov)

	
	v = array(eval(input("vetor2: ")))