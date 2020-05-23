from numpy import*
from numpy.linalg import*

mat = array(eval(input("Digite a matriz: ")))

vet = zeros(mat.shape[0])

for i in shape(mat):
	vet = sum(mat[i,:])

print(vet)

		