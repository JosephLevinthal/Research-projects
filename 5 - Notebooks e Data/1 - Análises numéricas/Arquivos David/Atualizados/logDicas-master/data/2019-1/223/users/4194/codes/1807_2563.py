from numpy import*
vet = array(eval(input("Medias: ")))
while (size(vet) > 1):
	ix = 0
	for i in range(size(vet)):
		if(5 <= vet[i] < 7):
			ix = ix + 1
	print(ix)
	vet = array(eval(input("Medias: ")))