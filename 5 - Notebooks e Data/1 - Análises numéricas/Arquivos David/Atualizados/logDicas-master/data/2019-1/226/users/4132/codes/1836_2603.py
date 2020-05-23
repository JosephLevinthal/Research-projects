from numpy import *
from numpy.linalg import *

m= array(eval(input("Digitte: ")))
v = zeros(shape(m)[1],dtype=int)
for i in range(4):
	for j in range(4):
		v[j] = m[j,i]
	v=sorted(v,reverse=True)
	for k in range(4):
		m[k,i]=v[k]
print(m)