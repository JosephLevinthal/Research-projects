from numpy import *
from numpy.linalg import *

mat = array(eval(input("H: ")))
m = shape(mat)[0]
t = zeros(m, dtype=int)

for i in range(m):
	t[i] = sum(mat[i,:])
print(t)