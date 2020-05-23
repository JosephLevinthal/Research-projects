from numpy import*
vet = array(eval(input("digite o vetor: ")))
while(size(vet)>1):
	alm = 0
	for x in vet:
		if(x >= 5)and(x < 7):
			alm = alm + 1
	print(alm)
	vet = array(eval(input("digite proximo vetor: ")))