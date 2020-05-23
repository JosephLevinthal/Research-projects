from numpy import *
vet = array(eval(input("digite o vetor: ")))
z = zeros(size(vet),dtype = int)
b = 0
c = 0
for i in range(size(vet)):
	if(vet[b] != 1):
		z[c] = vet[b]
		c = c + 1
	if(vet[b] == 1):
		z[c] = vet[b]
	b = b + 1
print(z)