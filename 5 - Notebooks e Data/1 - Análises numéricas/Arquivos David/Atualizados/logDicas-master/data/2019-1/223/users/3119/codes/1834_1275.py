from numpy import*
from numpy.linalg import*

mat = array(eval(input("Digite os valores: ")))

vet = zeros(mat.shape[0], dtype = int)

for i in range(mat.shape[0]):
	 vet[i] = sum(mat[i,:])
		
print(vet)		