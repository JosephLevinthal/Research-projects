from numpy import *

vet = array(eval(input("insira o vetor: ")))

cont = 0

while (cont <= (len(vet)-1)):
	if (vet[cont] >= 0):
		cont+=1

vetor = zeros(cont, dtype=int)

i = 0
o = 0

while (o < size(vetor)):
	if (vet[i] > 0):
		vetor[o] = vet[i]
		i+=1
		o+=1
	else:
		i+=1
print(vetor)