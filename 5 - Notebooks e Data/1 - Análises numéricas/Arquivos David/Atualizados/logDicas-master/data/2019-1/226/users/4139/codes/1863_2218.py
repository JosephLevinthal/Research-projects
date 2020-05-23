from numpy import*
from numpy.linalg import*

mat = array(eval(input("mat: ")))
soma = 0
for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if j > i:
			soma = soma + mat[i,j]

print(round(soma,2))