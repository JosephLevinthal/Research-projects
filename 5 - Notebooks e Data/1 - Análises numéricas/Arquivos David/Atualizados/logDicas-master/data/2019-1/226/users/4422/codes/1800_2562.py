from numpy import*

v = array(eval(input("1 vetor: ")))

while(size(v)>1):
	npar = 0
	
	for e in v:
		if(e%2==0):
			npar = npar + 1
	print(npar)
	
	print(size(v)- npar)
	
	print(size(v))
	
	v = array(eval(input("vetor2: ")))