from numpy import *

vet = array(eval(input("Insira o vetor: ")))
cont = 0
n = 0

for x in vet:
	if(x >= 0):
		n += 1
vetM = zeros(n, dtype=int)

for x in vet:
	if(x >= 0):
		vetM[cont] = x
		cont += 1
		
print(vetM)