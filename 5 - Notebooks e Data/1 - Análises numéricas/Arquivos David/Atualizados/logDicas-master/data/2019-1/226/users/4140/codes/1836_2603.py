from numpy import*
from numpy.linalg import*
mat=array(eval(input()))
a=shape(mat)[0]
b=shape(mat)[1]
for i in range(int(b)):
	mat[:,i]=sorted(mat[:,int(i)],reverse=True)
print(mat)
