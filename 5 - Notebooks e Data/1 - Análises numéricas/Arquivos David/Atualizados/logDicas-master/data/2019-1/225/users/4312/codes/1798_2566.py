from numpy import*
falt = array(eval(input("Faltas registradas: ")))

vet = zeros(6)

for i in range(0, size(falt)):
	
	if falt[i] == 2:
		vet[0] = vet[0] + 1
	elif falt[i] == 3:
		vet[1] = vet[1] + 1
	elif falt[i] == 4:
		vet[2] = vet[2] + 1
	elif falt[i] == 5:
		vet[3] = vet[3] + 1
	elif falt[i] == 6:
		vet[4] = vet[4] + 1
	else:
		vet[5] = vet[5] + 1

for i in range(0, size(vet)):
	vet[i] = round(vet[i]/size(falt) * 100, 1)

print(vet)
