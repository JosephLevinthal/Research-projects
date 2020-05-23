from numpy import*

vet = array(eval(input("Gols primeiro time: ")))
vet2 = array(eval(input("Gols segundo time: ")))
vet3 = zeros(3,dtype=int)

for i in range(size(vet)):
	if vet[i] > vet2[i]:
		vet3[0] = vet3[0] + 1
	elif vet[i] == vet2[i]:
		vet3[1] = vet3[1] + 1
	elif vet[i]< vet2[i]:
		vet3[2] = vet3[2] + 1
print(vet3)
	