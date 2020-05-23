from numpy import*
from numpy.linalg import*

mat = array(eval(input("Digite os valores: ")))

vet = zeros(mat.shape[0])

for i in range(mat.shape[0]):
	 vet[i] = max(mat[i,:])
	
i = 0

while(i < size(vet)):
	print(vet[i])
	i = i + 1