from numpy import*
from numpy.linalg import*

mat = array(eval(input("digite: "))) 

for j in range(shape(mat)[0]):
	x = (mat[j,:])
	print(max(x))