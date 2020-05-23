from numpy import *
from numpy.linalg import *
mat=array(eval(input("digite a matriz: ")))
ah= mat.shape [0]
b=zeros(ah, dtype=int)
for i in range(ah):
	b[i]=sum(mat[i,:])
print(b)
