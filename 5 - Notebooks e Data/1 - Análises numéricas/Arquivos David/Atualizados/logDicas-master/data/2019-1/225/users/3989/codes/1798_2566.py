from numpy import*

vet1 = array(eval(input("faltas: ")))
vet = zeros(6, dtype=float)
tam1 = size(vet1)
for i in range(tam1):
	if vet1[i] == 2:
		vet[0] = vet[0] + 1
	elif vet1[i] == 3:
		vet[1] = vet[1] + 1
	elif vet1[i] == 4:
		vet[2] = vet[2] + 1
	elif vet1[i] == 5:
		vet[3] = vet[3] + 1
	elif vet1[i] == 6:
		vet[4] = vet[4] + 1
	elif vet1[i] == 7:
		vet[5] = vet[5] + 1
for i in range(size(vet)):
	vet[i] = round((vet[i]*100/tam1), 1)
print(vet)