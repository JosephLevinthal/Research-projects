from numpy import *
from numpy.linalg import *
mat=array(eval(input("digite uma matriz: ")))
a=mat.shape [0]
b=zeros(a, dtype=int)
for i in range(a):
	b[i]=sum(mat[i,:])
for j in range(size(b)):
	if (b[j]==max(b)):
		print(j)

