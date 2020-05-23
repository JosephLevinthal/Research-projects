from numpy import*
from numpy.linalg import*

m = array(eval(input("matriz: ")))

c = 0
nl = shape(m)[0]
nc = shape(m)[1]
v = zeros(nc)
for i in range(nl):
	for j in range(nc):
		v[j] = m[i,j]
	c = c + min(v)
print(round(c/nl,2))