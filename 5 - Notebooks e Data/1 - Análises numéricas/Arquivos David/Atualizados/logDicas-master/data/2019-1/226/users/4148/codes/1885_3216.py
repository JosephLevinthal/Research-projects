from numpy import*
from numpy.linalg import*


a = array(eval(input('')))
b = array(eval(input()))


for i in range(size(a)):
	for j in range(size(b)):
		mat[i,j]= mat[a,b]
print(mat)
print()