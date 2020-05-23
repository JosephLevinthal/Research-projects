#ADRIANA BINDA LIMA

from numpy import *
vet = array(eval(input('Media: ')))

while (size(vet) > 1):
	ap = 0
	for elemento in vet:
		if (5 <= elemento < 7):
			ap = ap+1
		print(ap)
	