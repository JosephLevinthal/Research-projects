from numpy import *

vet = array(eval(input("vetor: ")))

cont = 0
acima = 0
while cont < size(vet):
	if vet[cont] > 99:
		print(cont)
		acima = acima + 1
	cont = cont + 1
print(acima)