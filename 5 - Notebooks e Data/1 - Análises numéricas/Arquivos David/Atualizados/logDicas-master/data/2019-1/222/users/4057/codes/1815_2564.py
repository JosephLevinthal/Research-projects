from numpy import*

vet1 = array(eval(input("gols efetuados em cada partida: ")))
vet2 = array(eval(input("gols levados em cada partida: ")))


while size(vet1) == size(vet2):
	a = 0
	cont = zeros(3, dtype = int)
	for i in (vet1, vet2):
		if (vet1[a] > vet2[a]):
			cont[0] = cont[0] +  1
		elif (vet1[a] == vet2[a]):
			cont[1] = cont[1] +  1
		elif(vet1[a] < vet2[a]):
			cont[2] = cont[2] +  1
	a = a + 1
	print(cont)
	vet1 = array(eval(input("gols efetuados em cada partida: ")))
	vet2 = array(eval(input("gols levados em cada partida: ")))