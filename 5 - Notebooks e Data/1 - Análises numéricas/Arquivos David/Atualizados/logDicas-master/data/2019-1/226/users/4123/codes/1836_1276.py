from numpy import*
from numpy.linalg import*
vet = array(eval(input()))
tot = zeros(shape(vet)[1],dtype = int)
for i in range(shape(vet)[0]):
	for j in range(size(tot)):
		tot[j] += vet[i,j]
for i in range(size(tot)):
	if tot[i] == max(tot):
		print(i+1)