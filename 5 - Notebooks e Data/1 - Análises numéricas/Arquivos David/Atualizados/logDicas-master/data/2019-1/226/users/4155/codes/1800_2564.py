from numpy import*
v1 = array(eval(input("v1: ")))
v2 = array(eval(input("v2: ")))

vet = zeros(3, dtype=int)

for i in range(size(v1)):
	if v1[i]>v2[i]:
		vet[0] = vet[0] + 1
	elif v1[i] == v2[i]:
		vet[1] = vet[1] + 1
	elif v1[i] < v2[i]:
		vet[2] = vet[2] + 1
print(vet)