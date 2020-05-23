from numpy import*
from numpy.linalg import*

mat = array(eval(input("digite: ")))
vet = zeros(shape(mat)[1],dtype=int)
for j in range(7):
	for i in range(shape(mat)[0]):
		vet[j] += mat[i,j]

for i in range(size(vet)):
	if vet[i] == max(vet):
		print(i+1)