from numpy import *
from numpy.linalg import *

mat = array(eval(input("")))
kkk = zeros(shape(mat)[0],dtype=int)

for i in range(size(kkk)):
	for j in range(7):
		kkk[i] +=mat[i,j]

print(kkk)