from numpy import*
from numpy.linalg import*

m = array(eval(input(": ")))
v = zeros(shape(m)[0], dtype=int)

for i in range(shape(m)[0]):
	for j in range(shape(m)[1]):
		v[j] = m[j,i]
	v = sorted(v, reverse=True)
	for j in range(shape(m)[1]):
		m[j,i] = v[j]
print(m)