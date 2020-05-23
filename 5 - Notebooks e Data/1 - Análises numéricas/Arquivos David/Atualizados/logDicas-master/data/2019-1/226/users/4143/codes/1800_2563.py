from numpy import*
vet = array(eval(input("vet aprovados:")))
aprovados= 0
i = 0
while (size(vet)>1):
	while (size(vet)>i):
		if (vet [i]<7) and (vet[i]>=5):
			aprovados+=1
		i+=1
	print(aprovados)
	vet = array(eval(input("vet aprovados:")))	
	aprovados= 0
	i = 0