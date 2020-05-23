from numpy import *
from numpy.linalg import *
m = array(eval(input("Digite: ")))
v = zeros(m.shape[0],dtype=float)
for i in range(m.shape[0]):
	for j in range(4):
		if (m[i,j] == min(m[i])):
			v[i] = v[i] + m[i,j]
a = sum(v)/size(v)
print(round(a,2))