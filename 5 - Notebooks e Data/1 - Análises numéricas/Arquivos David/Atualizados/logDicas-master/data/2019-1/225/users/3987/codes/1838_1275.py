from numpy import*
from numpy.linalg import *

mat = array(eval(input(":")))
qtdF = shape(mat)[0]
v = zeros(qtdF, dtype=int)
for i in range(qtdF):
	v[i] = sum(mat[i,:])
print(v)