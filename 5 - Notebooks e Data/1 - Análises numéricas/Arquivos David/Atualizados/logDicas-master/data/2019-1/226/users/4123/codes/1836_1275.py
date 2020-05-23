from numpy import*
from numpy.linalg import*
vet = array(eval(input()))
tot = zeros(shape(vet)[0],dtype = int)
tam = array([size(tot),shape(vet)[1]])
for i in range(size(tot)):
	for j in range(shape(vet)[1]):
		tot[i] += vet[i,j]
print(tot)