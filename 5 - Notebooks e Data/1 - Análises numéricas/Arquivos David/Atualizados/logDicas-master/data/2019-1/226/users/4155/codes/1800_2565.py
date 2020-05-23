from numpy import *
v1 = array(eval(input("v: ")))
v2 = array(eval(input("v: ")))
v3 = int(input("v: "))

vet = zeros(3, dtype=int)

for i in range(size(v1)):
	if v1[i] >= 5 and v2[i] >= v3 * (75/100):
		vet[0] = vet[0] + 1
	elif v1[i] < 5 and v1[i] >=0:
		vet[1] = vet[1] + 1
	elif v2[i] < v3 * (75/100):
		vet[2] = vet[2] + 1
print(vet)
		
		