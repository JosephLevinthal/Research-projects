from numpy import *
vet = array(eval(input("Vet: ")))
soma = 0
vet1 = zeros(soma, dtype=int)
for i in range(size(vet)):
	if (vet[i] < 5.0):
		soma = soma + 1
vet1 = zeros(soma, dtype=int)
for j in range(size(vet)):
	if (vet[j] < 5.0):
		vet1[j] = j
print(soma)
print(vet1)