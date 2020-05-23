from numpy import *

vet = array(eval(input("Vetor de Notas: ")))

while (len(vet)) > 1:
	monitor = 0
	
	for x in vet:
		if ( x >= 5) and (x < 7):
			monitor = monitor + 1
			
	print(monitor)
	
	vet = array(eval(input("Proximo vetor: ")))