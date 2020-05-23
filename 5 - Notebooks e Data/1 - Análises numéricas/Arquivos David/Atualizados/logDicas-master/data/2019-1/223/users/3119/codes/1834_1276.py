from numpy import*
from numpy.linalg import*

mat = array(eval(input("Digite os valores: ")))

vet = zeros(7, dtype = int)

for i in range(7):
	 vet[i] = sum(mat[:,i])

for i in range(7):
	if(vet[i] == max(vet)):
		print(i + 1)
		

		
