from numpy import*
vetor1 = array(eval(input("")))
vetor2 = array(eval(input("")))
vetor3 = zeros(size(vetor1))

cont = 0
cont1 = 1
cont2 = 0
while cont < size(vetor1):
	vetor3[cont] = vetor1[cont]/vetor2[cont]
	cont = cont + 1
while cont2 < size(vetor3):
	if vetor3[cont2] == max(vetor3):
		print(cont1)
	cont1 = cont1 + 1
	cont2 = cont2 + 1