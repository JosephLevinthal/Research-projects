from numpy import*
from numpy.linalg import*

mat = array(eval(input("digite: ")))

vet = zeros(shape(mat)[0],dtype=int)

for j in range(shape(mat)[0]):
	vet[j]= sum(mat[j,:])

print(vet)



