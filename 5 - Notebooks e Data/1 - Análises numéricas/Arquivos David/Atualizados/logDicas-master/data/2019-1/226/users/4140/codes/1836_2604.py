from numpy import*
from numpy.linalg import*
mat=array(eval(input()))
a=shape(mat)[0]
for i in range(a):
	b=max(mat[i,:])
	print(b)