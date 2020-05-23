from numpy import*
vet = array(eval(input('v: ')))

while size(vet) > 1:
	npar = 0
	for element in vet:
		if element % 2 == 0:
			npar += 1
	print(npar)
	print(size(vet)-npar)
	print(size(vet))
	vet = array(eval(input('v: ')))
	