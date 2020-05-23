from numpy import*
from numpy.linalg import*

mat = array(eval(input()))

s = 0
for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if i!=j:
			s += mat[i,j] 
			
print(round(s, 2))			