from numpy import*   
from numpy.linalg import*

mat = array(eval(input(" ")))

dias = zeros(shape(mat)[0], dtype=int)

for i in range(shape(mat)[0]):
	dias[i] = sum(mat[i,:])
print(dias)