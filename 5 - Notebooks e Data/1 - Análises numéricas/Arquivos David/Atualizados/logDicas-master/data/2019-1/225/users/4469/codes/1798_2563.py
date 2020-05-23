from numpy import*

vet = array(eval(input("Primeiro vetor: ")))

while (size(vet) > 1):
	s = 0

	for nota in vet:
		if(nota >= 5) and (nota < 7):
			s = s + 1

	print(s)

	vet = array(eval(input("Proximo vetor: ")))