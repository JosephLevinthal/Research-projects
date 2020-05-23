from numpy import *
from numpy.linalg import*

mat = array(eval(input()))
dias = zeros(shape(mat[1]), dtype=int)
				
for i in range(shape(mat)[1]):
	dias[i] = sum(mat[:, i])
		
for i in range(size(dias)):
	if(dias[i] == max(dias)):
		print(i + 1)