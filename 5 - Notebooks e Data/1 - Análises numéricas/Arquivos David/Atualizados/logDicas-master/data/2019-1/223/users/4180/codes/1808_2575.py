from numpy import*
vet = array(eval(input("Midias: ")))
resultado = zeros(3, dtype = int)

for i in range(size(vet)):
	if (vet[i]  == "TV"):
		resultado[0] = resultado[0] + 1
	elif(vet[i] == "NETFLIX"):
		resultado[1] = resultado[1] + 1
	elif(vet[i] == "YOUTUBE"):
		resultado[2] = resultado[2] + 1
print(resultado)
	