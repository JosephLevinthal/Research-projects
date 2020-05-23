from numpy import *
from numpy.linalg import *

mat= array(eval(input("digite a matriz: ")))
k = zeros(shape
for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if(i!=j):
			k[i]= mat[i,j]
print(min(k))