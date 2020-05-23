from numpy import*

vetA = array(eval(input("dados do primeiro time: ")))
vetB = array(eval(input("dados do time adversario: ")))

vet = zeros(3,dtype=int)

for x in range(size(vetA)):
	if(vetA[x] > vetB[x]):
		vet[0] = vet[0] +1
	if(vetA[x] < vetB[x]):
		vet[2] = vet[2] +1
	if(vetA[x] == vetB[x]):
		vet[1] = vet[1] +1
print(vet)