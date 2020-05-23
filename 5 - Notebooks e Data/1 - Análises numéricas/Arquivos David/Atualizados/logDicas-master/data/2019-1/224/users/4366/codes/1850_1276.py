from numpy import *
from numpy.linalg import *
mat=array(eval(input("digite a matriz: ")))
a= mat.shape [1]
b=zeros(a, dtype=int)
for j in range(a):
	b[j]= sum(mat[:,j])
for m in range(size(b)):
	if (b[m] ==max(b)):
		print(m+1)