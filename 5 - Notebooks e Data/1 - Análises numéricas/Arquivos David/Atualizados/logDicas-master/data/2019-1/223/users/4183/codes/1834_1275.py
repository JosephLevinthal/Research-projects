from numpy import *
from numpy.linalg import *
m = array(eval(input("Digite: ")))
v = zeros(m.shape[0],dtype=int)
for i in range(m.shape[0]):
	for j in range(7): 
		v[i] = v[i] + (m[i,j])
print(v)