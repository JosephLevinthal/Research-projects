from numpy import*

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: ")))

# Verifica se o programa vai terminar
npar = 0


while size(vet) > 1:
	for elemento in vet:
		if elemento % 2 == 0:
			npar = npar + 1
	nimpar = size(vet) - npar
   # No. de elementos pares
	print(npar)

   # No. de elementos impares
	print(nimpar)

   # No. total de elementos
	print(size(vet))
	npar = 0
	nimpar = 0

   # Leitura do proximo vetor
	vet = array(eval(input("Proximo vetor: ")))

