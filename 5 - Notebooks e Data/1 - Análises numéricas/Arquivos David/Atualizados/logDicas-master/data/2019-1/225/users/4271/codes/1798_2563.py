from numpy import *
vet = array(eval(input("Vetor com as notas: ")))
while (size(vet) > 1):
	nmonitor = 0
	for x in vet:
		if (x >= 5 and x < 7):
			nmonitor = nmonitor + 1
	print(nmonitor)
	vet = array(eval(input("Proximo vetor: ")))