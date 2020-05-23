from numpy import *
vet = array(eval(input('primeiro vetor: ')))
while(size(vet)>1):
	nmonitor = 0
	for elemento in vet:
		if (elemento >= 5 and elemento <7):
			nmonitor += 1
	print(nmonitor)
	vet = array(eval(input('proximo vetor: ')))