from numpy import*

vet = array(eval(input("Notas: ")))

while (size(vet) > 1): 
	m = 0
	for elemento in vet:
		if (elemento  >=5 and elemento < 7):
			m = m + 1
	print(m)
	vet = array(eval(input("Notas: ")))
