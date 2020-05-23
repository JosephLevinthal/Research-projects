from numpy import*

vet1 = eval(input("digite: "))
vet2 = zeros(vet1, dtype= int)

cont = 0
j = -1

for i in range(len(vet1)):
	if vet1[i] != 1:
		vet2[cont] = vet1[i]
		cont = cont + 1 
	else:
		vet2[j] = vet1[i]
		j = j - 1
print(vet2)
