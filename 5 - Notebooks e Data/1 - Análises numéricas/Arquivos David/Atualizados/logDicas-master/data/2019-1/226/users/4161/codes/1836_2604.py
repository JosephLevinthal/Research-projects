from numpy import*
from numpy.linalg import*

m= array(eval(input(": ")))
v = zeros(shape(m)[0])
v2 =zeros(shape(m)[1])
a = 0
b = 0
for i in range(size(v)):
	for j in range(7):
		v2[j] = m[i,j]
	v[i] = max(v2)
for i in range(size(v)):
	print(v[i])