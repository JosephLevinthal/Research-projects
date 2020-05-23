from numpy import *
vet = array(eval(input("Vetor de notas: ")))
while (size(vet) > 1):
	soma = 0
	for i in vet:
		if ((i >= 5) and (i < 7)):
			soma = soma + 1
	print(soma)
	vet = array(eval(input("Vetor de notas: ")))	