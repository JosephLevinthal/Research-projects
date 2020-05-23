from numpy import*
from numpy.linalg import*

mat =array(eval(input("digite: "))) 

a = 0
for j in range(shape(mat)[0]):
	x = (mat[j,:])
	a += min(x)
print(round(a/shape(mat)[0], 2))