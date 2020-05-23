from numpy import *
from numpy.linalg import *
mat = array(eval(input("Matriz quadrada: ")))
n = shape(mat)[0]
ed = (n**2 - n)//2
vet = zeros(ed, dtype = float)
k = 0
for i in range(n):
	for j in range(n):
		if i < j:
			vet[k] = mat[i,j]
			k = k + 1

print(max(vet))

