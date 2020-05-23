from numpy import*
from numpy.linalg import*
mat = array(eval(input("vv: ")))
m = shape(mat)[0]
q = zeros(m, dtype=int)

for i in range(m):
	q[i] = sum(mat[i,:])
print(q)