from numpy import *
from numpy.linalg import *
mat=array(eval(input("matriz: ")))
s=mat.shape[0]
z=zeros(s,dtype=int)
for i in range (s):
	z[i]=sum(mat[i,:])
print(z)