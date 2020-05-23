from numpy import*
vet = array(eval(input("TV, NETFLIX e YOUTUBE:")))
vtei = zeros(3, dtype=int)

for i in range(size(vet)):
	if (vet[i] == "TV"):
		vtei [0] = vtei[0] + 1
	elif (vet[i] == "NETFLIX"):
		vtei[1] = vtei[1] + 1
	elif(vet[i] == "YOUTUBE"):
		vtei[2] = vtei[2] + 1
print(vtei)


