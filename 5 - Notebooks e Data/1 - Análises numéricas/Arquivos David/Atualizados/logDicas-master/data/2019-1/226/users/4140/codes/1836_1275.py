from numpy import*
from numpy.linalg import*
mat=array(eval(input()))
a=shape(mat)[0]
mat2=zeros(a,dtype=int)
for i in range(a):
	mat2[i]=sum(mat[i,:])
print(mat2)

