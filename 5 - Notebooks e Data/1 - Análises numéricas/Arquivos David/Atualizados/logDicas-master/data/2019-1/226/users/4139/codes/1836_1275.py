from numpy import*
from numpy.linalg import*

mat = array(eval(input("digite: ")))
vet = zeros(shape(mat)[0],dtype=int)

for i in range(size(vet)):
	for j in range(7):
		vet[i] += mat[i,j]
print(vet)