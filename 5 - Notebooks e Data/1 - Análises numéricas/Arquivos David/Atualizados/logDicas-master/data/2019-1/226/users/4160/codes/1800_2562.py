from numpy import*

v = array(eval(input("Vetor: ")))

while(size(v)>1):
	npar = 0
	for i in v:
		if(i % 2 == 0):
			npar = npar + 1
	print(npar)
	print(size(v)- npar)
	print(size(v))
	v = array(eval(input("Vetor: ")))

	
