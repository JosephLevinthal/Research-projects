from numpy import*

vet = array(eval(input("digite: ")))

while (size(vet)>1):
	aux = 0
	for i in vet:
		if (i >= 5) and (i<7):
			aux = aux + 1
	print(aux)
	vet = array(eval(input("digite: ")))